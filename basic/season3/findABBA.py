# txt = "ABBBBBABABBA";
txt = input("Enter your Input: ")
seperatedArray = []
listTxt = list(txt)

for i,item in enumerate(listTxt):
  if i%4 == 0:
    seperatedArray.append(item+listTxt[i+1]+listTxt[i+2]+listTxt[i+3]);

flag = False

for item in seperatedArray:
  if item == "ABBA" or item == "BAAB":
    flag = True

if flag:
  print("YES");
else:
  print("NO");

