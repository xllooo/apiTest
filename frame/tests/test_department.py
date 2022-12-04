import pytest

from frame.apis.department.department import Department


class TestDepartment:
    def setup_class(self):
        self.Department = Department()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('name, parentid, id, order,result', [
        ('业务测试一组', 2, 101, 999901, 999901),
        ('业务测试二组', 2, 102, 999902, 999902),
        ('业务测试三组', 2, 103, 999903, 999903)
    ])
    def test_create_department(self, name, id, parentid, order, result):
        self.Department.create_department(name=name, parentid=parentid, id=id, order=order)
        try:
            r = self.Department.get_department_by_id(id=id, parentid=parentid)
        finally:
            self.Department.delete_department(id=id)
        assert r == result

    @pytest.mark.parametrize('name, parentid, id, order,result', [
        ('业务测试一组', 2, 101, 999901, 999901),
        ('业务测试二组', 2, 102, 999902, 999902),
        ('业务测试三组', 2, 103, 999903, 999903)
    ])
    def test_find_department(self, name, id, parentid, order, result):
        self.Department.create_department(name=name, parentid=parentid, id=id, order=order)
        try:
            r = self.Department.get_department_by_id(id=id, parentid=parentid)
        finally:
            self.Department.delete_department(id=id)
        assert r == result

    @pytest.mark.parametrize('name, parentid, id, order,result', [
        ('业务测试一组', 2, 101, 999901, 999901),
        ('业务测试二组', 2, 102, 999902, 999902),
        ('业务测试三组', 2, 103, 999903, 999903)
    ])
    def test_update_department(self, name, id, parentid, order, result):
        self.Department.create_department(name=name, parentid=parentid, id=id, order=order)
        try:
            self.Department.update_department(id=id, order=order)
            order = self.Department.get_department_by_id(id=id, parentid=parentid)
        finally:
            self.Department.delete_department(id=id)
        assert order == result

    @pytest.mark.parametrize('name, parentid, id, order,result', [
        ('业务测试一组', 2, 101, 999901, None),
        ('业务测试二组', 2, 102, 999902, None),
        ('业务测试三组', 2, 103, 999903, None)
    ])
    def test_delete_department(self, name, id, parentid, order, result):
        self.Department.create_department(name=name, parentid=parentid, id=id, order=order)
        self.Department.delete_department(id=id)
        order = self.Department.get_department_by_id(id=id, parentid=parentid)
        assert order == result
