from page.xueqiu_app import Xueqiu_APP


class Xueqiu_Testcase():
    def setup(self):
        Xueqiu_APP.start()

    def test_load(self):
        pass

    def teardown(self):
        Xueqiu_APP.close()