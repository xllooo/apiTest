import requests

from frame.utils.log_utils import logger


class Base:
    def __init__(self):
        pass

    def send_api(self, req, dolog: bool = True):
        res = requests.request(**req)
        if dolog is True:
            logger.info(f'接口发送的数据为{req}')
            logger.info(f'接口相应的数据为{res.json()}')
        return res
