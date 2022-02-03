#qshqshqsh为你量身打造
#setstate
import os
import random
import datetime
#玩家属性:第一项玩家位置 第二项生命 第三项伤害 第四项盔甲防御 第五项蓝 第六项饥饿值 第七项等级
manboxA = [0,100,5,10,180,100,0]
#群系物品设定 物品编码
mapboxwp = [[10,17,18,25],[18,19,22,25,26,27],[24,25,26,27,28],[18,23,24,25],[10,17,18,27,28],[18,19,22,23,24]]
#群系生物设定 生物名称
mapboxsw = [["史莱姆","滑稽","万草枯"],["可爱小骨头","网抑云矿工","万骨枯"],["我不是·人","矿石精","操蛇之神"],["踩了一脚珍贵地貌的游客","彩虹铲屎官","彩虹猫"],["狗头","奇怪知识猫","量子的使者"],["核辐射下长腿的鲨鱼","飞鱼队","垃圾袋护体波塞冬"]]
#各种生物属性 ps：第一项是血量，第二项是技能名称，第三项是技能伤害，第四项是简介orz,
#第五项是生成概率

#应该不会有人来维护罢，，下面这些代码我自己都看不懂，屎山了，上一条ps完全没用，抓紧时间删库跑路叭，公司没有年终奖（笑）
swbox = [[[30,[["撞击",5],["分裂包围",7]],"绿色的球球，不断跳动，是玩家不变的信仰",[0,80],20],[40,[["迷惑一笑",7],["呼唤水军",12]],"跟着我，嘴角上扬，看向右方",[80,95],30],[55,[["啊我哭了",10],["召唤草魂",15],["落日斩",20]],"你见过我那在象墓山谷的哥哥嘛（这是该地区的boss级生物）",[95,100],40]],[[30,[["扑进怀",5],["成群结队",10]],"拉起手，在阳光下，有群小骨头",1],[45,["敲你",8],"emo,emo",3]]]
#群系名称
mapnumber = ["落日平原","象墓山谷","无人山地","艳美丹霞","奇异空岛","鲨滩海岸"]
#物品名称
bagname = ["木剑","石剑","骨剑","铜剑","铁剑","银剑","金剑","钻石剑","亡魂剑","雌雄双股剑","苹果","面包","苹果派","蘑菇煲","肥宅快乐水","青菜煲","炸肉","木材","石材","骨头","肉","蘑菇","丝线","沙石","铜","铁","银","金","钻石"]

zb = "手"
#bagnumber第一项表示数量，第二项表示属性，第三项表示成效
bagnumberA = [[1,1,10],[0,1,15],[0,1,20],[0,1,30],[0,1,35],[0,1,40],[0,1,45],[0,1,50],[0,1,55],[0,1,65],[0,2,3],[1,2,8],[0,2,10],[0,2,12],[0,2,15],[0,2,20],[0,2,20],[0,0,0],[0,0,0],[0,0,0],[0,2,2],[0,2,2],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
def inshelp():
    print("输入 $朕 可以查看自己的所有属性。")
    print("输入 $朕的东西 可以查看自己的背包物品。")
    print("输入 $装备  可以将武器装备到手上。")
    print("输入 $用膳  可以将食物吃下。")
    print("输入 $朕来看看 对当前地区进行搜索。")
    print("输入 $起驾 可以离开或前往某区域")
    print("输入 $退出 可以结束该程序")
    print("输入 $保存 可以保存当前进度（测试中不保证稳定，报错不要慌张）")
           
    return 0

def insinput():
    global zb
    global name
    
    ins = input("请输入下一步指令")
    if ins == "$朕":
        print("您的生命值为",manbox[1])
        print("您的饥饿值为",manbox[5])
        print("当前装备",zb)
        print("您一次普通攻击对敌人造成伤害为",manbox[2])
        print("您的盔甲防御值为",manbox[3])
        print("您目前的蓝（你懂得）为",manbox[4])
        print("您目前的等级为",manbox[6])
    elif ins == "$朕的东西":
        for x in range(len(bagname)):
           print(x+1,"号",bagname[x],bagnumber[x][0],"个")
           print()
    elif ins == "$装备":
        whatfight = input("请输入要装备的物品编号")
        if bagnumber[int(whatfight)-1][1] == 1:
            zb = bagname[int(whatfight)-1]
            manbox[2] = bagnumber[int(whatfight)-1][2]
            print("装备成功，当前装备",zb)
        else:
            print("此物品不可装备，只能装备武器哦(^_^)")
    elif ins == "$用膳":
        whateat = input("请输入要吃的物品编号")
        if bagnumber[int(whateat)-1][1] == 2:
            manbox[5] = manbox[5] + bagnumber[int(whateat)-1][2]
            print("呕吼！！！成功食用，当前饥饿值",manbox[5])
        else:
            print("此物品不可食用，只能吃食物哦(^_^)")
    elif ins == "$救驾":
        inshelp()
        
    elif ins == "$起驾":
        print("请问您要前往哪里？（请输入序号）")
        for mapmap in range(len(mapnumber)):
            print(mapmap+1,"号地区",mapnumber[mapmap])
           
        wheretogo = input("请问您想要去哪里鸭，请输入序号")
        
        if int(wheretogo) >=1 and int(wheretogo) <= 6:
            
            manbox[0] = int(wheretogo) - 1
            print("成功抵达目的地，您当前在",mapnumber[manbox[0]])
            
        else:
            print("哪有这个这序号")
    
    elif ins == "$退出":
        print("成功退出")
        
        exit()
    elif ins == "$保存":
        while True:
            dirname=input("请输入存档名:")
            path="/storage/emulated/0/ASG/save/"
            if not os.path.exists(path):
                os.mkdir(path)
            cdpath=path+dirname+".txt"
        
            if os.path.exists(cdpath):
                print("该存档名已存在！")
            else:
                break
        file=open(cdpath,"w")
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\n"+name+"\n")
        for i in manbox:
            file.write(str(i)+",")
        file.write("\n")
        for i in bagnumber:
            file.write(str(i)+",")
        file.close()
        exit()
    elif ins == "$朕来看看":
        findt = random.randint(1,100)
        if findt < 80:
            #以下出现过报错 2022.2.1
            #原因找到了，只给了randint一个参数
            findwp = random.randint(0,len(mapboxwp[manbox[0]])-1) 
            print("恭喜(*^_^*)，您获得了一个",bagname[mapboxwp[manbox[0]][findwp]])
            bagnumber[findwp][0] = int(bagnumber[mapboxwp[manbox[0]][findwp]][0]) + 1
        else:
            findsw=random.randint(1,100)
       #2022.2.1补充(包括上一行)
            zz1=0
            while True:
                if findsw<swbox[manbox[0]][zz1][3][1] and findsw>=swbox[manbox[0]][zz1][3][0]:
                    break
                zz1=zz1+1
            #交战生物
            swzz=mapboxsw[manbox[0]][zz1]
            swzzxl=swbox[manbox[0]][zz1][4]
            print("哦！您遇到了",swzz,"以下是它的简介:",swbox[manbox[0]][zz1][2],"，[血量:",swzzxl,"]")
            inp1=input("请问是否与之交战(Y/N)")
            if inp1== "Y" or inp1=="y":
                while True:
                    
                    #生物技能暂存
                    jineng=random.randint(0,len(swbox[manbox[0]][zz1][1])-1)
                    if random.randint(0,1) == 1:
                        print(swzz,"对您使用了",swbox[manbox[0]][zz1][1][jineng][0],"对您造成了",swbox[manbox[0]][zz1][1][jineng][1],"点伤害")
                        manbox[1]=manbox[1]-swbox[manbox[0]][zz1][1][jineng][1]
                    else:
                        print(swzz,"对您使用了",swbox[manbox[0]][zz1][1][jineng][0],"未命中")
                    if random.randint(0,1)==1:
                        print("您使用",zb,"对",swzz,"进行了常规攻击","对其造成",manbox[2],"点伤害")
                        swzzxl=swzzxl-manbox[2]
                    else:
                        print("您使用",zb,"对",swzz,"进行了常规攻击，但未命中")
                    if swzzxl <=0 :
                        print("恭喜您击败了",swzz)
                        break
                    elif manbox[1] <= 0:
                        print("GAME OVER")
                        exit()
            else:
                   #生物技能暂存
                    jineng=random.randint(0,len(swbox[manbox[0]][zz1][1])-1)
                    #交战生物追击逃跑玩家
                    if random.randint(0,1) == 1:
                        print(swzz,"对您使用了",swbox[manbox[0]][zz1][1][jineng][0],"对您造成了",swbox[manbox[0]][zz1][1][jineng][1],"点伤害")
                        manbox[1]=manbox[1]-swbox[manbox[0]][zz1][1][jineng][1]
                    else:
                        print(swzz,"对您使用了",swbox[manbox[0]][zz1][1][jineng][0],"未命中")
                

                   
'''            firstcent = 10 * (-0.014 * int(manbox[2]) + 0.7)
            secondcent = float(firstcent) + 10 * (0.002 * int(manbox[2]) + 0.3)
            thirdcent = float(secondcent) + 10 * (0.006 * int(manbox[2]))
            fourthcent = float(thirdcent) + 10 * (0.006 * int(manbox[2]))
            findsw = random.randint(1,10)
            if float(findsw) >=1 and float(findsw) <= float(firstcent):
                print("哦！您遇到了",mapboxsw[manbox[0]][0],"下面是它的简介")
                print()
         
        
        '''
        
            #以上代码作废，因为不知道什么意思
        #如果你能看懂，，那也别碰了

            
#game first start . setstate ending .        
      
def nextt():
    manbox[5] = manbox[5] - 3
    print("****************分割线****************") 
    return 0  
#Beginning.
print("⠀⠀⠀⠀⠀⢰⣿⣦")
print("⠀⠀⠀⠀⠀ ⠛⠿⠃⣀⣤⣀")
print("⠀⠀⠀⣠⣿⣿⣿⣷⣿⣿⣿⣿⣿⡀")
print("⠀  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧")
print("⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟")
print("⠀⠀ ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁")
print("⠀⠀⠀  ⠙⢿⣿⣿⡿⠿⠟") 
for i in range(7):
    print(" *",end="")
    
print("")
    
print("*浆果夹工作室*")

for i in range(7):
    print(" *",end="")
    
print("")
print("--------------ASG--------------\n--------A Shadiao's Game--------")
dudu=input("1号 新的游戏\n2号 选择存档继续游戏\n输入序号进行选择")
cs=1001
manbox=manboxA
bagnumber=bagnumberA
yn=""
if dudu=="1":
    
    
    yn = input("您第一次玩吗？(请输入Y/N)(本游戏中所有Y/N不注重大小写)")
    
    name = input("向导：探险者，请输入您的姓名：")

    print("向导：",name,"?真是个尊贵高冷又不失沙雕的名字呢。")

#写个开始写了那么长orz

    if yn == "Y" or yn== "y":
            print("向导：既然你是第一次来，那我就教教你基本操作。您可以输入 $救驾 来获得帮助。")
            
elif dudu=="2":
   if not os.path.exists("/storage/emulated/0/ASG/save"):
                os.mkdir("/storage/emulated/0/ASG/save")
   print("请选择存档文件:")
   print("┏/storage/emulated/0/ASG/save")
   for file in os.listdir("/storage/emulated/0/ASG/save"):
       print("┣"+file)
   cundang=input("请输入要加载的存档文件名(不用加txt后缀)")
   f="/storage/emulated/0/ASG/save/"+cundang+".txt"
   data=open(f,"r")
   zz2=0
   for line in data:
              zz2=zz2+1
              if zz2==3:
                  manbox=line.split(",")
              if zz2==4:
                  bagnumber=line.split(",")

for baba in range(0,cs):
    insinput()
    print("你还有",1000-int(baba),"次行动机会！")
    nextt()
        
        
        
print("游戏结束啦啦啦(✪▽✪)感谢游玩")
exit()
     



    
                    

     

