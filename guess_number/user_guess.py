import random

def guess(max_num):
    random_num = random.randint(1,max_num)
    guess = 0

    while guess!=random_num:
        guess = int(input(f"Guess the number between 1 and {max_num}: "))
        if guess > random_num:
            print('Too high, try agian bro')
        elif guess < random_num:
            print('Too low a number, try again homie')
        
    print(f"Yey, congrats. You have guess the number {random_num}")

guess(10)

