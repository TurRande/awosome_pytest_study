def test_001():
    print("这是test001测试用例")


def test_002():
    try:
        print("-" * 15, "欢迎来到烤鸭店", "-" * 15)
        price1 = int(input("请输入烤鸭的进货价:"))
        price2 = int(input("请输入烤鸭的卖货价:"))
        num = int(input("请输入今日卖出的烤鸭数量:"))
        price3 = (price2 - price1) * num
        print("烤鸭店今日的利润为:{}元".format(price3))
    except Exception as err:
        print("您输入的烤鸭价格或者数量不对,请您重新输入")
