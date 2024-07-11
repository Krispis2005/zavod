import random
import time
import datetime

time.sleep(30)
def dangerous_situation () :
    dt = datetime.datetime.now()
    long = random.uniform(0.1, 35)
    people = random.randint (1,10)
    a = random.random()
    stroka = str(dt) +' ' + str(long) +' ' + str(people)
    if a <= 0.4 :
        with open('logs.txt', 'a') as f:
            f.write(stroka)
        return True
    return False

dangerous_situation()



