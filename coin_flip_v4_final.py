import random, time, math

def stats():
    head_count = 0
    total_count = 0
    max_count = 1000000
    consec_count = 0
    top_count = 0

    start = time.time()
    while total_count < max_count:
        total_count += 1
        if random.choice([True, False]):
            head_count += 1
            consec_count += 1
            if consec_count > top_count:
                top_count = consec_count
        else:
            consec_count = 0

    finish = time.time()
    percentage = round((head_count / total_count) * 100, 2)
    tot_time = math.ceil(finish - start)
    prob = 0.5 ** top_count
    print(f'''This was a project to see how many times a coin could consecutively land on heads
in a given amount. In this case, the total count was {total_count}. A total of {head_count}
coins landed on heads, giving a final percentage of {percentage}. The largest streak of heads, or
the consecutive amount of heads, was {top_count} which is about a {round(prob, 10)}% chance.
This process took roughly {tot_time} second.''')

stats()

# This is my final refactor for now. I did a complete rehaul of this one and focused
# on presentation. I think it looks a bit nicer, though it does limit it to boolean
# where the others could be expanded to multiple options, perhaps weighted flips
# for example. Perhaps I will revisit one day.
