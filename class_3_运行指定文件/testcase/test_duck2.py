def test10():
    """
    烤鸭店利润计算器
    """
    try:
        print('***** 烤鸭店利润计算器开始运行 *****')
        print('-------------------------------')
        price1 = int(input('请输入每只烤鸭的进货价:'))
        price2 = int(input('请输入每只烤鸭的售卖价:'))
        num = int(input('请输入今天售卖的烤鸭数量:'))
        result = (price2 - price1) * num
        print("您今天的利润为{}元".format(result))
    except Exception as err:
        print("您输入的数量或者价格有误,请您重新输入:")