import inspect
import json
from collections import Callable
from typing import List, NamedTuple, Any

from mako.template import Template
from pydantic import BaseModel

from src.data.models.business.request import Response
from src.data.models.transform.event_to_request import event_to_request


def endpoint(endpoint, methods):
    def wrapper_endpoint(func):
        func._route = endpoint
        func._methods = methods
        return func

    return wrapper_endpoint


class Endpoint(NamedTuple):
    route: str
    methods: List[str]
    func: Callable

    def match(self, endpoint: str, method: str):
        return self.route.lower() == endpoint.lower() and method in self.methods  # make it easier


def _create_wrapper(method):
    function_signature = inspect.signature(method)

    def wrapper(request, **kwargs):
        new_kwargs = kwargs.copy()
        for key, param in function_signature.parameters.items():
            param_annotation = param.annotation
            if issubclass(param_annotation, BaseModel):
                request_json = json.loads(request.body)
                new_value = param_annotation(**request_json)
                new_kwargs[key] = new_value
            else:
                new_value = request.parameters.get(key, None)
                if new_value:
                    new_kwargs[key] = new_value

        return method(**new_kwargs)

    return wrapper


class BaseHandler:
    def __init__(self, request_transformation=event_to_request):
        super(BaseHandler, self).__init__()

        # self.logger = getLogger(__class__)
        self.endpoints = []
        self._request_transformation = request_transformation

        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            route = getattr(method, '_route', None)
            if route:
                https_methods = getattr(method, '_methods', None)
                current_endpoint = Endpoint(route, https_methods, _create_wrapper(method))
                self.endpoints.append(current_endpoint)

    # TODO extract out later since need more hadlers in one lambda
    def handle(self, event, context):
        request = self._request_transformation(event)
        for endpoint in [x for x in self.endpoints if x.match(request.endpoint, request.method)]:
            return endpoint.func(request=request)

        return self.common_handle(request)

    def make_response(self, content: Any, status_code, headers={}) -> Response:
        strigified_body = content.json() if isinstance(content, BaseModel) else json.dumps(content)
        return Response(body=strigified_body, statusCode=status_code, headers=headers).dict()

    def make_html_response(self, content: Any, status_code=200, headers={}) -> Response:
        strigified_body = content.render() if isinstance(content, Template) else str(content)

        return Response(body=strigified_body, statusCode=status_code, headers=headers).dict()

    def common_handle(self, request):
        raise NotImplementedError
