# txt = "testaaaTKHKH"
txt = input("put ur shit here: ")
upperCount = 0;
lowerCount = 1;

for item in list(txt):
  if item.isupper():
    upperCount+=1
  else:
    lowerCount+=1

if upperCount>lowerCount:
  print(txt.upper())
else: 
  print(txt.lower())