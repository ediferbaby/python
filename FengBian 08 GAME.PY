import random
import time
level=input("请输入你要挑战的级别：(1-10)")
while int(level)<1 or int(level)>10:
	level=input("请正确输入挑战的级别：(1-10)")

#定义NPC的属性
npc_random=random.randint(100,200)/100
npc_life=10*int(level)*npc_random
npc_attack=5*int(level)*npc_random

#定义PLAYER属性
player_random=random.randint(100,200)/100
player_life=10*int(level)*player_random
player_attack=5*int(level)*player_random

#打印NPC和PLAYER的属性

print("NPC的随机数:"+str(npc_random),end='')
print("PLAYER的随机数:"+str(player_random))


print("NPC的生命值:"+str(npc_life),end='')
print("PLAYER的生命值:"+str(player_life))


print("NPC的攻击力:"+str(npc_attack),end='')
print("PLAYER的攻击力:"+str(player_attack))

time.sleep(1)
n=0
while npc_life>0 and player_life>0:
    
    n=n+1
    print('第'+str(n)+'轮')
    
    print('NPC的生命值'+str(npc_life)+'-'+str(player_attack)+'='+str(npc_life-player_attack))
    npc_life=npc_life-player_attack
    #
    print('PLAYER的生命值'+str(player_life)+'-'+str(npc_attack)+'='+str(player_life-npc_attack))
    player_life=player_life-npc_attack
    time.sleep(1)

print('！！！游戏结束！！！')
print('NPC的生命值还有'+str(npc_life))
print('PLAYER的生命值还有'+str(player_life))

if npc_life>0:
    print('WINNER IS NPC')
else:
    print('WINNER IS PLAYER')      



