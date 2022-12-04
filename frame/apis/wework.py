from frame.apis.base import Base
from frame.utils.utils import Utils


class WeWork(Base):
    def __init__(self):
        super(WeWork, self).__init__()
        yaml_data = Utils.get_yaml_data("../datas/corp_data.yaml")
        self.token = self.get_token(corpid=yaml_data.get("corpid"),
                                    corpsecret=yaml_data.get("secret").get("department"))

    def get_token(self, corpid: str = None, corpsecret: str = None) -> str:
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        res = self.send_api(req=req, dolog=False)
        token = res.json().get('access_token')
        return token


if __name__ == '__main__':
    print(WeWork())
