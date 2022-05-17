n = int(input("how many times we should run: "));
listOfData = []
answer = []

for i in range(0,n):
  d = input("insert data:");
  d = d.split(" ")
  listOfData.append({
    d[0] : d[1]
  })

yourString = input("what is yout text: ").split(' ');


def calculator(array):
  for i,el in enumerate(array):
    key = list(el.keys())[0]
    value = list(el.values())[0]
    if yourString[i] == key:
      answer.append(value);
    elif yourString[i] == value:
      answer.append(key)
  return answer


print(" ".join(calculator(listOfData)));