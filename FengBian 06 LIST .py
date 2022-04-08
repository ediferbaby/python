import random

#list=random.sample(range(50,100),8)
list=[11,22,33,44,55,66]

print (list)

for n in list:
    print(n)

#option=input("请输入你要删除的第N个内容:")

#del list[int(option)-1]
#print (list)

scores={"China":"中国","Russia":"俄罗斯"}   #字典
#print(scores['China'])
for i in scores:
    print(scores[i])    #China为键,中国为值，打印值
    print(i)            #打印键

print(len(scores))  #长度
