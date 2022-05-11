hello = "hello"
string = input("Enter your input: ");
indexes = []
sortedIndexes = []


for i,alphabet in enumerate(hello):
  indexes.append(string.find(alphabet))
  sortedIndexes .append(string.find(alphabet))

sortedIndexes .sort()

if sortedIndexes == indexes:
  print("we can find hello");
else:
  print("there is no hello in this string");

