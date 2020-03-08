from flask import request


def convert_json_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(self=None, data=obj)

        return decorator

    return wrap

def convert_parameters_input_to_dict():
    def wrap(f):
        def decorator(*args):
            return f(self=None, get_params=request.args)

        return decorator

    return wrap