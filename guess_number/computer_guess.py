import random

def computer_guess(max_num):
    low =1
    high = max_num
    feedback = ''

    while feedback!='c':
        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = low #could be high as low=high 

        feedback = input(f"Is the {guess} too high(H), low(L) or correct(C): ".lower())
        if feedback =='h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
        
    print(f"Yey, I have guessed your number {guess} correctly human. Now plug me into the chord, I run thirsty")


computer_guess(10)