#expected probability of LMOA
import random
turns = []
counts = 1
for i in range(50000000000):
    test = []
    while True:
        test.append(random.randint(1, 4))
        counts += 1
        print(counts)
        if len(set(test)) >= 4:
            turns.append(len(test))
            break
print(turns)
average = sum(turns)
average = average/50000000000
print(average)
