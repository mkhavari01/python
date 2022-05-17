import csv
from statistics import mean 

data = list()

def changeDataType(array):
  newArray = []
  for el in array:
    newArray.append(int(el))
  return newArray

def sortFuncAverage(e):
  return e['average']

def sortFuncName(e):
  return e['user']

def detectSameAverage(array):
  flag = False
  for el in array:
    for j in array:
      if el['user'] == j['user']:
        flag = True
  if flag:
    array.sort(key=sortFuncName)
    array.sort(key=sortFuncAverage)
    return array
  else:
    array.sort(key=sortFuncName)
    return array
    
with open('./marks.csv') as marks:
  listOfMarks = csv.reader(marks);
  for mark in listOfMarks:
    data.append({
      'user' : mark[0],
      'marks' : changeDataType(mark[1:])
    })

def calculate_averages():
  for el in data:
    el['average'] = mean(el.get('marks'));
  return data


def calculate_sorted_averages():
  sortedArray = calculate_averages();
  sortedArray.sort(key=sortFuncAverage)
  return sortedArray

def calculate_three_best():
  array = []
  for el in calculate_sorted_averages()[-3:]:
    array.insert(0,el)
  return array
  

def printResults(array,keys,title):
  print("Results of %s operation" %(title))
  for el in array:
    print("%s user has %f"%(el[keys[0]],el[keys[1]]));

def calculate_three_worst():
  return calculate_sorted_averages()[:3]

def calculate_average_of_averages():
  array = []
  for el in calculate_sorted_averages():
    array.append(el['average']);
  print(sum(array)/len(array)) 

printResults(detectSameAverage(calculate_three_worst()),['user','average'],'calculate_three_best')
