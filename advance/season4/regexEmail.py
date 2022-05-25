import re

txt = input("Enter your Email: ")
regex = r"[A-Za-z0-9]+[-._]?[A-Za-z0-9]+@[a-z]*[.]{1}[a-zA-z]*"
pat = re.compile(regex)

def check(email):
  if(re.fullmatch(pat, email)):
    print("Valid Email")
  else:
    print("Invalid Email")

check(txt)