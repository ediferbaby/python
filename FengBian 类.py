#--------------------------------------------
class Computer:
    screen = True

    def start(self):
        print('电脑正在开机中……')

my_computer = Computer()
print(my_computer.screen)
my_computer.start()


#--------------------------------------------
class Chinese:

    def born(self, name, birthplace):
        print(name + '出生在' + birthplace)

    def live(self, name, region):
        print(name + '居住在' + region)

person = Chinese()
person.born('吴枫','广东')
person.live('吴枫','深圳')

#--------------------------------------------
class Chinese:
    def __init__(self,name,hometown,region):
        self.name=name
        self.hometown=hometown
        self.region=region

    def Pname(self):
        print('我叫%s。'% self.name)
    def born(self):
        print('我出生在%s。' % self.hometown)
    def live(self):
        print('我是%s人。'%self.region)

wufeng = Chinese('Ethan','SZ','广东')
wufeng.Pname()
wufeng.born()
wufeng.live()


#-----------------------------------------------------
class Chinese:
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% area)

class Cantonese(Chinese):
    # 直接对方法进行重写
    def land_area(self,area):
        print('我们的祖国有%s万平方公里的陆地面积。'%area)
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% int(area * 0.0188))

aa=Cantonese()       
aa.land_area(960)