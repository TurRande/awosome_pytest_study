class Test01:
    @classmethod
    def setup_class(cls):
        """
        类方法中的前置操作,作用为每个类运行之前执行
        :return:
        """
        print("这是[类方法]的前置操作")

    @classmethod
    def teardown_class(cls):
        """
        类方法中的后置操作,作用为每个类运行之后执行
        :return:
        """
        print("这是[类方法]的后置操作")

    def test01(self):
        print("这是类Test01中的测试方法test01")

    def test02(self):
        print("这是类Test01中的测试方法test02")