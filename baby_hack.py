import random

# constants
gen = 10000
count = 100
days = 365


# break close all  cycle, so i put one iter to funk
def iteration():
    have_same_day = 0
    # birthday of baby's
    babys = [random.randrange(days) + 1 for _ in range(count)]

    for ind, baby in enumerate(babys):
        for o_ind, o_baby in enumerate(babys):
            # if it's not the same child
            if ind != o_ind and baby == o_baby:
                have_same_day = 1
                break
    return have_same_day


def cycle():
    all_days = 0
    for i in range(gen):
        all_days += iteration()
    print(all_days / gen)

cycle()