from numpy import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper ='''
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

computer_ch_index = random.randint(0,2) # To generate radnom number b/w 0 To 2.
choice = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while user_choice>=3 or user_choice <0:
    print("You Typed a invalid number, You Lose ")
    print("Try Again")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
      
print(f"You chose: {choice[user_choice]}")

print(f"Computer chose: {choice[computer_ch_index]}")


if user_choice == computer_ch_index:
    print("It's a draw!")
elif (user_choice == 0 and computer_ch_index == 2) or (user_choice == 1 and computer_ch_index == 0) or (user_choice == 2 and computer_ch_index == 1):
    print("You win!")
else:
    print("You lose!")
    




