while True:
    try:
        # 当 int() 修饰的时候，如果放置的内容不是数字，那就会 break
        num1 = int(input("请输入第一个数字: "))
        num2 = int(input("请输入第二个数字: "))
        result = num1 + num2
        print("结果为：", result)
        break
    except ValueError:
        print("输入的值不是数字，请重新输入")
    except KeyboardInterrupt:
        print("退出～")
        break
