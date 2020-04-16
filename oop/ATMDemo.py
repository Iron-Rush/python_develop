# ATMDemo.py
# ATM排队等待实例
import random
# ATM类
class ATM():
    def __init__(self, maxtime = 5):
        # 办理一个业务的最长时间
        self.t_max = maxtime
    # 计算完成本次业务所需的时间
    def getServCompleteTIme(self, start = 0):
        return start + random.randint(1, self.t_max)

# Customers类
class Customers():
    # n为总体的客户数量
    def __init__(self, n):
        self.count = n  #全部客户数量
        self.left = n   #剩余客户数量
    # 下一个客户到达ATM的时间
    def getNextArrvTime(self, start = 0, arrvtime = 10):
        if self.left != 0:
            self.left -=1
            return start + random.randint(1, arrvtime)
        else:
            return 0
    def isOver(self):
        return True if self.left == 0 else False

if __name__ == "__main__":
    c = Customers(100)
    a = ATM()
    # 等待队列、等待时间
    wait_list = []
    wait_time = 0
    cur_time = 0    #当前时间
    cur_time += c.getNextArrvTime()
    wait_list.append(cur_time)
    while len(wait_list) != 0 or not c.isOver():
        if wait_list[0] <= cur_time:
            next_time = a.getServCompleteTIme(cur_time) #下次时间.
            del wait_list[0]
        else:
            next_time = cur_time + 1

        if not c.isOver() and len(wait_list) == 0:
            next_arrv = c.getNextArrvTime(cur_time)
            wait_list.append(next_arrv)

        if not c.isOver() and wait_list[-1] < next_time:
            next_arrv = c.getNextArrvTime(wait_list[-1])
            wait_list.append(next_arrv)
            while next_arrv < next_time and not c.isOver():
                next_arrv = c.getNextArrvTime(next_arrv)
                wait_list.append(next_arrv)
        for i in wait_list:
            if i <= cur_time:
                wait_time += next_time - cur_time
            elif cur_time < i < next_time:
                wait_time += next_time - i
            else:
                pass
        cur_time = next_time
    print(wait_time/c.count)

