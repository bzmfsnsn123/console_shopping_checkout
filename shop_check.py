def shopping():
    goods={1:("矿泉水",2),2:("面包",5),3:("牛奶",4),4:("薯片",7),5:("可乐",3),6:("汉堡",7),7:("薯条",5),8:("好多鱼",5),9:("辣条",1),10:("鸡腿",4)}
    cart=[]
    print("=====便利店结算系统=====")
    print("商品列表：")
    for k,v in goods.items():
        print(f"{k}.{v[0]}单价{v[1]}元")
    while True:
        print("\n功能：1.选购商品 2.查看购物车&总价 3.结算结账 0.退出")
        try:
            op=int(input("请输入功能序号："))
            if op==1:
                num=int(input("输入商品序号："))

                if num not in goods:
                    print("商品不存在!")
                else:
                    name,price=goods[num]
                    cart.append(price)
                    print(f"已加入：{name}")

            elif op==2:
                if not cart:
                    print("购物车空空如也！")
                else:
                    total=sum(cart)
                    print(f"当前商品总价为：{total}元")
                    print(f"选购件数{len(cart)}件")


            elif op==3:
                if not cart:
                    print("暂无商品，无法结账")
                else:
                    total=sum(cart)
                    print(f"本次结算总金额：{total}元，结账完成！")
                    cart.clear()
                    print("购物车已清空")
            elif op==0:
                print("欢迎下次光临，程序结束。")
                break
            else:
                print("请选择序号0-3")
        except ValueError:
            print("请输入数字序号")
if __name__=="__main__":
    shopping()