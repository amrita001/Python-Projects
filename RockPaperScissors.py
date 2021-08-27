import random

 #r > s , s > p , p > r
 #Players get only 5 chances

def StartGame():
     point1=0
     point2=0
     print('# r for rock \n# p for paper \n# s for scissors')
     for round in range(5):     #5 times the loop will run
         user = input('\nEnter your choice: ')
         computer = random.choice(['r', 'p', 's'])
         print("Computer's choice: "+computer)

         print(f'Round{round+1} result:', end='\t')
         if(user==computer):
            print("Oops it's a tie!")

         elif(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
            print("Congrats, you won!!")
            point1=point1+1

         else:
            print("You lost!")
            point2=point2+1

     if(point1==point2):
         print(f'\n[ You and Computer both have won! ]')
     elif(point1>point2):
            print(f'\n[ You won in {point1}/5 rounds ]')
     else:
            print(f'\n[ Computer won in {point2}/5 rounds ]')




StartGame()   # Calling the function
