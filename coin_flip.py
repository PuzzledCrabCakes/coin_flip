import random

def stats():
    count = 0
    total = 0
    consecutive = 0
    while True:
        num = ['h', 't']
        loop = random.choice(num)

        print(loop)
        for i in loop:
            total = total + 1

        if loop == 'h':
            count = count + 1
            consecutive = consecutive + 1

            if consecutive == 10:
                break
        else:
            consecutive = 0
    print(f'The amount of heads flipped was: {count} at {(count / total) * 100}%')
    print(count, total)

stats()
