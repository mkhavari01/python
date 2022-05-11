# test = "11212+21+03+1+-2"
data = input("enter whatever you want dude: ");

def changeDataToStr(list):
  newList = []
  for item in list:
    newList.append(str(item))
  return newList

def finalData(list):
  newList = []
  for item in list:
    newList.append(int(item))
  newList.sort()
  return changeDataToStr(newList)

data = finalData(data.split("+"))

print("data is ","+".join(data))