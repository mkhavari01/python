class School:
  def __init__(self,name):
    self.name = name;
    self.ages = [];
    self.heights = [];
    self.weights = [];
  
  def set_datas(self):
   School.set_heights(self);
   School.set_ages(self);
   School.set_weights(self);
   School.set_result(self);

  def set_heights(self):
    heights = input("Enter your heights: ");
    for el in heights.split(" "):
      self.heights.append(float(el));
  def set_ages(self):
    ages = input("Enter your ages: ");
    for el in ages.split(" "):
      self.ages.append(float(el));
  def set_weights(self):
    weights = input("Enter your weights: ");
    for el in weights.split(" "):
      self.weights.append(float(el));

  def set_result(self):
    self.heightsResult = sum(self.heights)/len(self.heights);
    self.weightsResult = sum(self.weights)/len(self.weights);
    self.agesResult = sum(self.ages)/len(self.ages);
  def get_result(self):
    yield self.heightsResult
    yield self.weightsResult
    yield self.agesResult

a = School('A');
b = School('B');

a.set_datas();
b.set_datas();

A = [0,13];
B = [1,2]

for i in a.get_result():
  A.append(i)
  print(i)

for i in b.get_result():
  B.append(i)
  print(i)

def compareResult(A,B):
  for index,el in enumerate(A):
    if el > B[index]:
      print("A");
      return
    elif el < B[index]:
      print("B")
      return
    elif el == B[index]:
      print("SAME")
      return

compareResult(A,B)