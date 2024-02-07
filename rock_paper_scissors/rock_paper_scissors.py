import random

def rock_paper_scissors():
       while True:
        user = input(f"Please chose your move, rock(r), paper(p), scissors(s)")
        bot = random.choice(['r','p','s'])
        if user == bot:
            print(f'Your choise {user} and computers choice {bot} was the same. Try again')
            continue
        elif (user == 'r' and bot =='s') or (user == 's' and bot =='p') or (user == 'p' and bot =='r'):
            print('You win')
        else:
            print('You Lose')
           
        print(f"computers choise was {bot}")
        break
    
rock_paper_scissors()