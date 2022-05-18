from datetime import datetime

userDate = input('Enter ur freaking birth time: ').split("/");

today = str(datetime.today()).split(" ")[0].split("-");

for index,el in enumerate(today):
  today[index] = int(el);
  userDate[index] = int(userDate[index])

if(userDate[0]>today[0]):
  print("WRONG");
elif userDate[1] > 12 :
  print("WRONG");
elif userDate[2] > 31:
  print("WRONG");

print(today[0] - userDate[0])