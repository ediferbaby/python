for i in '吴承恩':
    print(i)

dict = {'日本':'东京','英国':'伦敦','法国':'巴黎'}
for i in dict:
    print(dict[i]+"在"+(i))

k=0
while k < 4:
    k=k+1
    print(k)

for i in range(1,11,3):
    print(str(i)+"*5="+str(i*5))



#9*9乘法表
print("--------------9*9乘法表-----------------")
for i in range(1,10):
    
    for j in range(1,i+1):
        #print(j*i)
        #print("j="+str(j))
        print(str(j)+"*"+str(i)+"="+str(i*j)+'\t',end=' ')
    print('')    


print('1234\tabc')
    


