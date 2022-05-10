allAges = []
age = int(input("Enter an age: "));

while age != -1:
  allAges.append(age);
  age = int(input("Enter another age: "));

print("The Oldest one is: ",max(allAges))

allAges.remove(max(allAges))

print("The second Oldest one is: ",max(allAges))