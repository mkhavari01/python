import random

randomNumber = int(random.randrange(1,9));
answer = int(input("Guess the computer number: "));

while answer != randomNumber : 
  print("you are sick bro");
  if answer > randomNumber:
    print("the number that you've guessed was bigger");
  else :
    print("the number that you've guessed was smaller");
  answer = int(input("Guess the computer number again: "));
    

print("Mashallah Broher you did it");