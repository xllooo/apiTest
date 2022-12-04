from frame.apis.wework import WeWork


class Department(WeWork):

    def create_department(self, name: str, parentid: int,
                          id: int, order: int):
        req = {
            'method': 'POST',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
            'params': {
                'access_token': self.token
            },
            'json': {
                'name': name,
                'parentid': parentid,
                'id': id,
                'order': order
            }
        }
        res = self.send_api(req=req)
        return res.json()

    def update_department(self, id: int, order: int):
        req = {
            'method': 'POST',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
            'params': {
                'access_token': self.token
            },
            'json': {
                "id": id,
                "order": order,
            }
        }
        res = self.send_api(req=req)
        return res.json()

    def get_department_simple_list(self,
                                   parentid) -> list:
        department_simple_list = list()
        req = {
            'method': 'GET',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/department/simplelist',
            'params': {
                'id': parentid,
                'access_token': self.token
            }
        }
        res = self.send_api(req=req)
        for department_list in res.json().get('department_id'):
            if department_list.get('parentid') == parentid:
                department_simple_list.append(department_list)
        return department_simple_list

    def get_department_by_id(self, id: int,
                             parentid: int):
        department_simple_list = self.get_department_simple_list(parentid=parentid)
        for department in department_simple_list:
            if department.get('id') == id:
                order = department.get('order')
                return order
        return None

    def delete_department(self, id: int):

        req = {
            'method': 'GET',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/department/delete',
            'params': {
                'id': id,
                'access_token': self.token

            }
        }
        res = self.send_api(req=req)
        return res.json()
