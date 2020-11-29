class BaseController:
    def __init__(self, template_prefix="./", base_controller=""):
        self._template_prefix = template_prefix
        self._base_controller = base_controller

    def _get_view(self, view):
        return f"{self._base_controller}_{view}" if view is not None else self._base_controller

    def _get_data(self, **kwargs) :
        raise NotImplementedError

    def _get_by_id(self, id):
        raise NotImplementedError
