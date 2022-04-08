#-----------文件读写------------------
#----直接改写
#file1 = open('D:/out.txt','w',encoding='utf-8') #参数w，可写内容，直接改写

#file1.write('写入行1\n')   #写入内容

#file1.close()

#------------------只读
file2=open('D:/out.txt','r',encoding='utf-8')
file2content=file2.read()

#print(file2content)

file2.close()
#------------添加内容
file3=open('D:/out.txt','a',encoding='utf-8')   #参数a,可写入内容，在最后添加
#file3.write('附加模式，此行为最后一行。\n')
file3.close()
#------------逐行读取
file4=open('D:/out.txt','r',encoding='utf-8')
file_court=file4.readlines()
file4.close()

print(file_court)
final_scores=[]
for i in file_court:
    data=i.split()
    #print(data)
    sum=0
    for score in data[1:]:
        sum=sum+int(score)

    result=data[0]+str(sum)
    print(result)

    final_scores.append(result)

winner=open('D:/out11.txt','a',encoding='utf-8')
winner.writelines(final_scores)
winner.close


