points = [3,1,0,1,3];
wins = 0;
totalPoint = 0

for point in points:
  if point == 3:
    wins+=1;
  totalPoint += point

print("they could have take ",totalPoint,"points from ",len(points),"games and they won ",wins," game ")