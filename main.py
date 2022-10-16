import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
c=[rock,paper,scissors]
i=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print ("Your choice:\n",c[i])
r=random.randint(0,2)
print("Computer choice:\n",c[r])
if(i==0 and r==2):
  print("You win")
elif(i==2 and r==1):
  print("You win")
elif(i==1 and r==0):
  print("You win")
elif(i==r):
  print("Match draw")
else:
  print("You lose")
  
