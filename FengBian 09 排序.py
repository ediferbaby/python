list1 =  [91, 95, 97, 99]  
list2 =  [92, 93, 96, 98]

print('方法1：')
for i in list2:
    list1.append(i) #把list2的值逐个添加到list1
    print(list1)


print('方法2：')
list1 =  [91, 95, 97, 99]  
list2 =  [92, 93, 96, 98]
list1.extend(list2) #把list2的值一次添加到list1的结尾
print(list1)

list1.sort()        #从小到大排列
print(list1)

#计算总和
count=0
for i in list1:
    #print(i)
    count=count+i
print('总和是:'+str(count))

#计算平均数
print('平均数是:'+str(count/len(list1)))

#计算低于平均数
list3=[]
for j in list1:
    if j<count/len(list1):
        print('低于平均分的有:'+str(j))
        list3.append(j)

print(list3)
