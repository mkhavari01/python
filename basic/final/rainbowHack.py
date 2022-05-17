import csv
import hashlib

data = [];
hashData = {}

with open('./passwords.csv') as passwords:
  listOfPasswords = csv.reader(passwords);
  for password in listOfPasswords:
    data.append({
      password[1] : password[0]
    })

for i in range(1000,9999):
  hashData[hashlib.sha256(str(i).encode('utf-8')).hexdigest()]= i

def printPasswords(array):
  for el in array:
    print("%s password is %s" %(list(el.values())[0],hashData[list(el.keys())[0]]))

printPasswords(data)