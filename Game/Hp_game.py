# -*- coding: utf-8 -*-#
# @Time : 2020/10/27 0:04 
# @Author : fgc
# @File : Hp_game.py
# -*- coding: utf-8 -*-#
# @Time : 2020/10/26 0:05
# @Author : fgc
# @File : Hp_game.py


"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 定义一个fight的方法
import random


def fight(hp, power):

    #   初始化敌人的血量数据
    enemy_hp = random.choice(hp)
    enemy_power = random.choice(power)
    print(f"敌人的初始血量为{enemy_hp}")
    print(f"敌人的攻击力为{enemy_power}")
    print("------------------------------------------------------")

    # 初始化自己的血量和攻击力
    my_hp = random.choice(hp)
    my_power = random.choice(power)
    print(f"我的初始血量为{my_hp}")
    print(f"我的攻击力为{my_power}")
    print("------------------------------------------------------")

    # 添加游戏循环
    while True:
        # 添加游戏的血量计算规则
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        #   添加游戏的输赢规则
        if my_hp > enemy_hp:
            # 打印我和敌人的血量
            print("分出胜负了,游戏结束")
            print(f"我的剩余血量为:{my_hp}")
            print(f"敌人的剩余血量为:{enemy_hp}")
            print("我赢了")
            # 跳出循环
            break

        if my_hp <= enemy_hp:
            # 打印我和敌人的血量
            print("分出胜负了,游戏结束")
            print(f"我的剩余血量为:{my_hp}")
            print(f"敌人的剩余血量为:{enemy_hp}")
            print("敌人赢了")
            # 跳出循环
            break


if __name__ == '__main__':
    # 初始化血量和攻击力数据
    hp = [x for x in range(100, 150)]
    power = [y for y in range(20, 30)]
    # 调用游戏方法
    fight(hp, power)
