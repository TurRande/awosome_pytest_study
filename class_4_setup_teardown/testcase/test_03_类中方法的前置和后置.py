class Test02:
    @classmethod
    def setup_class(cls):
        print("这是[类的]前置")

    @classmethod
    def teardown_class(cls):
        print("这是[类的后置]")

    def setup_method(self):
        print("这是类中[方法]的前置")

    def teardown_method(self):
        print("这是类中[方法]的后置")

    def test01(self):
        print("这是 [Test02] 类中的测试用例 [test01] ")

    def test02(self):
        print("这是 [Test02] 类中的测试用例 [test02] ")