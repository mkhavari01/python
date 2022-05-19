class Human:
  def __init__(self,name):
    self.name = name

class Player(Human):
  pass
  def get_name(self):
    print(self.name)

playersA = []
playersB = []
names = ["حسین" , "مازیار" , "اکبر" , "نیما" ,  "مهدی" , "فرهاد" , "محمد" , "خشایار" , "میلاد" , "مصطفی" , "امین" , "سعید" , "پویا" , "پوریا" , "رضا" , "علی" , "بهزاد" , "سهیل" , "بهروز" , "شهروز" , "سامان" , "محسن"]

for i in range(0,22):
  if i <= 10:
    playersA.append(Player(names[i]));
    playersA[i].get_name()
  else:
    playersB.append(Player(names[i]));

