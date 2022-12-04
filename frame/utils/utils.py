import os

import yaml


class Utils:

    @classmethod
    def get_yaml_data(cls, yaml_file):
        with open(f"{Utils.get_data_path()}/{yaml_file}", encoding="utf-8") \
                as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_data_path(cls):
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../data"])
        return path

    @classmethod
    def get_log_path(cls):
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../logs"])
        return path

    # @classmethod
    # def jsonpath_util(cls, obj, expr):
    #     return jsonpath.jsonpath(obj, expr)
