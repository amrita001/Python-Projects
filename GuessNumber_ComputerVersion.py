import random

def guess_num(x):
   low=1
   high=x
   feedback=''
   while(feedback != 'c' and high!=low):
        num = random.randint(low,high)
        feedback = input(f'Is {num} too high(H), too low(L) or correct(C) ').lower()
        if(feedback=='h'):
            high=num-1
        elif(feedback=='l'):
            low=num+1
   print(f'Yay! The computer has guessed the number {num} correctly!')

guess_num(50) #Range is 50, any number can be given here acc to user's choice
