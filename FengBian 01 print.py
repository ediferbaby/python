import time
import random
import string

#print ('在'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'，我写了人生中第一行Python代码\n它的内容虽然简单，不过是平凡的一句print(520)\n但我知道：我的编程之路，将从最简单的520开始\n在我点击运行的同时，一切在这一刻开始变得不同\n以下，是这行代码的运算结果：' )

print( "整数型随机数:"+str(random.randint(1,10)))        # 产生 1 到 10 的一个整数型随机数  
print( "随机浮点数:"+str(random.random() ) )            # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(0,100,3) )   # 生成从0到100的间隔为5的随机整数

a=[4,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(str(a)+'打乱的元素顺序')

print(type(1))
print( type(random.uniform(1.1,5.4) ) )

print ('1-50随机数'+str(random.randint(1,50)))    # 1-50随机整数：

print (random.randrange(0, 101, 2))   # 随机选取0到100间的偶数：

# 随机浮点数：
print (random.random())
print (random.uniform(1, 10))

# 随机字符：
print ("随机字符："+random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))

# 多个字符中生成指定数量的随机字符：
print ("随机生成指定数量的字符:"+str(random.sample('zyxwvutsrqponmlkjihgfedcba',5)))

# 从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (ran_str)

# 多个字符中选取指定数量的字符组成新字符串：
print (''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 随机选取字符串：
print (random.choice(['剪刀', '石头', '布']))

# 打乱排序
it = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(it)
print (it)