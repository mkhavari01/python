from datetime import datetime

# userDate = input('Enter ur freaking birth time: ').split("/");

# today = str(datetime.today()).split(" ")[0].split("-");

# for index,el in enumerate(today):
#   today[index] = int(el);
#   userDate[index] = int(userDate[index])

# if(userDate[0]>today[0]):
#   print("WRONG");
# elif userDate[1] > 12 :
#   print("WRONG");
# elif userDate[2] > 31:
#   print("WRONG");

# print(today[0] - userDate[0])


class Age(datetime):
  def __init__(self):
    pass

  def set_data(self):
    self.userDate = input('Enter ur freaking birth time: ').split("/");

  def get_today(self):
    self.today = str(datetime.today()).split(" ")[0].split("-");
    
  def get_result(self):
    Age.set_data()
    Age.get_today()
    Age.change_dataType()
    if(self.userDate[0]>self.today[0]):
      print("WRONG");
    elif self.userDate[1] > 12 :
      print("WRONG");
    elif self.userDate[2] > 31:
      print("WRONG");
  
  def change_dataType(self):
    for index,el in enumerate(self.today):
      self.today[index] = int(el);
      self.userDate[index] = int(self.userDate[index])

ali = Age();
ali.get_result()