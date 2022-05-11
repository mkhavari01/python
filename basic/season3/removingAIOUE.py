string = input("put any shit u want: ");

callableAlphabetLower = 'aeuio';
callableAlphabetUpper = 'AEUIO';

indexes = []

def replace(index,string):
  string = list(string);
  for index in indexes:
    string[index] = "";
  return "".join(string)


for i,alphabet in enumerate(string):
  if callableAlphabetLower.find(alphabet) != -1 or callableAlphabetUpper.find(alphabet) != -1:
    indexes.append(i)
  
print(replace(indexes,string))