#try........except
while True:
    try:
        age = int(input('你今年几岁了？'))
        break
    except ValueError:
        print('你输入的不是数字！')


if age < 18:
    print('不可以喝酒噢')


#
