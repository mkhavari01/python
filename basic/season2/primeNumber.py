from xmlrpc.client import boolean


number = int(input("Enter a number: "));

primeNumber = boolean(number%2 != 0);

if primeNumber:
  print("it is Prime Number");
else :
  print("it is Even Number");

