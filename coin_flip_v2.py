import random
import time
import math

def stats():
    count = 0
    total = 0
    consecutive = 0
    start = time.time()
    while True:
        num = ['h', 't']
        loop = random.choice(num)
        #print(loop)
        for i in loop:
            total = total + 1
        if loop == 'h':
            count = count + 1
            consecutive = consecutive + 1
            if consecutive == 20:
                break
        else:
            consecutive = 0
    percentage = (count/total) * 100
    finish = time.time()
    print(f'The amount of heads flipped was: {count} out of {total} at {round(percentage, 2)}%')
    print(math.ceil(finish - start))
    return percentage

results1 = stats()
print(round(results1))
results2 = stats()
print(round(results2))
results3 = stats()
print(round(results3))

# This one runs the experiment three times
