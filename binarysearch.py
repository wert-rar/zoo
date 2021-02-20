import math
import time
import random


def bin_metod(r_number, min_n, max_n):
    count = 0
    while True:
        guess_n = min_n + (max_n - min_n) // 2
        print('i guess it ', guess_n)
        count += 1
        if r_number < guess_n:
            max_n = guess_n
            print('no it less')
        elif r_number > guess_n:
            min_n = guess_n
            print('no it greater')
        else:
            print()
            print('yes it is ', r_number)
            break
        time.sleep(0.5)
    return count



def main():
    max_number = 1000000
    print('max number of guess: ', int(math.log2(max_number)) + 1)
    print()
    print('create number for 0 to ', max_number)
    random_number = random.randint(1,max_number)
    print('count of g', bin_metod(random_number, 0, max_number))


if __name__ == "__main__":
    main()
