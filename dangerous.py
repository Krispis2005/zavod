import random
import time
import datetime

time.sleep(30)
f = open('xyz.txt','w')
def dangerous_situation (dt, long, people) :
    dt = datetime.datetime.now()
    long = random.uniform(0.1, 35)
    people = random.randint (1,10)
    if random.random() > 0.4 :
        return "Ложное срабатывание"
    return "Опасная ситуация"
    f.write(dt, long, people)
f.close()




