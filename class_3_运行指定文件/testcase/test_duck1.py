class Test30:
    def test_30(self):
        print("烤鸭店利润计算器开始工作")
        while True:
            price1 = int(input("请输入你的进货价："))
            price2 = int(input("请输入你的售卖价："))
            #　input传递来的值，都是str
            profits = price2 - price1
            if profits < 5 or profits >= 20:
                print("价格定价不合理，不能售卖！")
                continue
            num = int(input("请输入你今天卖的鸭子数量："))
            result = (price2 - price1) * num
            print("今天你的利润额度为{}=元".format(result))
            break

    def test_40(self):
        print("这是测试用例40")