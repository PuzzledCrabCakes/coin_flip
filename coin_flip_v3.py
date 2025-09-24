import random
import time
import math

def stats():
    count = 0
    total = 0
    consecutive = 0
    score = 0
    start = time.time()
    while total <= 4999999:
        num = ['h', 't']
        loop = random.choice(num)
        #print(loop)
        for i in loop:
            total = total + 1
        if loop == 'h':
            count = count + 1
            consecutive = consecutive + 1
            if consecutive > score:
                score = consecutive
            if consecutive == 26:
                break
        else:
            consecutive = 0
    percentage = (count/total) * 100
    finish = time.time()
    print(f'The amount of heads flipped was: {count} out of {total} at {round(percentage, 2)}%')
    print(f'This step took {math.ceil(finish - start)} seconds')
    print(f'The longest streak of heads flipped was {score}!')

stats()

# A minor refactor with an emphasis on finding the longest streak if target not met
