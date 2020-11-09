'''
完全不懂算法和多线程，着实没太搞懂这一部分，
参照着网上的资料和其他人的作业总算是得出了一个结果，但显然有些问题
'''
import threading
import queue
import time
import random

class DiningPhilosophers(threading.Thread):
    def __init__(self,index,count,q,left,right):
        super(DiningPhilosophers,self).__init__()
        self.index = index
        self.count = count
        self.q = q
        self.leftfork = left
        self.rightfork = right
    
    def run(self):
        while self.count>0:
            # pickLeftFork = self.leftfork.acquire(timeout=1)
            # if pickLeftFork:
            #     self.pickLeftFork()
            # else:
            #     countinue
            # pickRightFork = self.rightfork.acquire(timeout=1)
            # if pickRightFork:
            #     self.pickRightFork()
            #     self.dining()
            #     self.putDownLeft()
            #     self.putDownRight()
            #     self.count-=1
            # else:
            #     self.putDownLeft()
            self.pickLeftFork()
            self.pickRightFork()
            self.dining()
            self.putDownLeft()
            self.putDownRight()
            self.count-=1

    def pickLeftFork(self):
        self.leftfork.acquire()
        self.q.put([self.index,1,1])
    
    def pickRightFork(self):
        self.rightfork.acquire()
        self.q.put([self.index,2,1])
            
    def putDownLeft(self):
        self.q.put([self.index,1,2])
        self.leftfork.release()

    def putDownRight(self):
        self.q.put([self.index,2,2])
        self.rightfork.release()

    def dining(self):
        time.sleep(random.uniform(1,3)/1000)
        self.q.put([self.index, 0, 3])

    def think(self):
        time.sleep(random.uniform(1,3)/1000)


if __name__ == '__main__':
    count = int(input('请输入就餐次数n:\n'))
    q = queue.Queue()
    forks = [threading.Lock() for i in range(5)]
    philosophers = [DiningPhilosophers(i,count,q,forks[i],forks[(i+1)%5]) for i in range(5)]
    
    for philosopher in philosophers:
        philosopher.start()
    
    for philosopher in philosophers:
        philosopher.join()
    
    log_file = []
    while True:
        log_file.append(q.get())
        if q.empty():
            break
    
    print(log_file)
    
