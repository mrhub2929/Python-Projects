import random
INPUT = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")




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

randoms = [rock,paper,scissors]
assignment = random.randint(0,2)
s = randoms[assignment]




if INPUT == '0':
    print(rock)
    print(s)
    if s == 0:
        print("Tie")
    elif s == 1:
        print("You Lose")
    elif s == 2:
        print("You win")


elif INPUT == '1':
    print(paper)
    print(s)
    if s == 0:
        print("You win")
    elif s == 1:
        print("Tie")
    elif s == 2:
        print("You Lose")

else:
    print(scissors)
    print(s)
    if s == 0:
        print("You Lose")
    elif s == 1:
        print("You Win")
    elif s == 2:
        print("Tie")
