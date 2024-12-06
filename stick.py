

print("Welcome to stick game!!!"
      "\nto play a sticks game in which there are 16 sticks. "
      "\nTwo players take turns to play the game. "
      "\nEach player picks one set of sticks (needn’t be adjacent) during his turn."
      "\nA set contains 1, 2, or 3 sticks."
      "\nThe player who takes the last stick is the loser.")


person1=input("Enter the name of player 1:")
person2=input("Enter the name of player 2:")
stick=16
while stick!=0:
   print("Remaining stick",stick)
   choice=int(input(f"{person1}:The number of sticks player can take 1,2 or 3:"))
   stick=stick-choice
   player=person1
   if stick>=0:
      print( "remaining stick:",stick)
      choice = int(input(f"{person2}:The no: of sticks player can take 1,2 or 3:"))
      stick=stick-choice
      player=person2
      if stick<=0:
           print(f"{player} is the loser.")


