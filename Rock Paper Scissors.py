#Rock Paper Scissors
import random
import time
name=str(input("What's your name?"))
print("Hey",name,"want to play rock paper scissors??")
time.sleep(0.5)
s=input("Type \'yes\' to play  or \'no\' to leave the game")
if s.lower()=="no":
    exit
elif s.lower()=="yes":
   print("Then lets start!!!")
   time.sleep(1)
   a=["rock","paper","scissors"]
   print("Your choices are" ,a)
   while s.lower()=="yes":
      print("...........................................................................................")
      p=str(input("Choose an item or type \'exit\' to leave"))
      c=random.choice(a)
      time.sleep(1)
      if p.lower()=="rock":
         print("I chose",c)
         if c=="paper":
             print("You Lose :(")
         elif c=="rock":
            print("Its a tie!!")
         elif c=="scissors":
            print("You Win :) !!!!")
      elif p.lower()=="paper":
            print("I chose",c)
            if c=="paper":
                print("Its a tie!!")
            elif c=="rock":
                print("You Win :) !!!!")
            elif c=="scissors":
                print("You Lose :(")
      elif p.lower()=="scissors":
            print("I chose",c)
            if c=="scissors":
                print("Its a tie!!")
            elif c=="paper":
                print("You Win :) !!!!")
            elif c=="rock":
                print("You Lose :(")
      elif p.lower()=="exit":
          break
      else:
          print("Enter a valid option :|")

   

        
             
   
