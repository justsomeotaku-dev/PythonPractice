import random, sys, time

WIDTH = 70

try:
    cols = [0]*WIDTH
    while True:
        for i in range(WIDTH): # 70 times
            if random.random() < 0.02: # 0.0 <= X < 1.0
                cols[i] = random.randint(4,14)
            if cols[i] == 0:
                print(' ', end='')
            else:
                print(random.choice([0,1]), end='')
                cols[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
