import random
import string

number = random.randint(1,100)

#print(number)

if number>=90:
    print( str(number)+"成绩大于90，优秀")

elif number<30 :
    print(str(number)+"学渣，没救了。！！")

elif number >60:
    print( str(number)+"及格了，继续努力")
else :
    print(str(number)+"不及格，要努力哈。")


