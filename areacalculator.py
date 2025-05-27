
print("AREAA CALCULATOR!!!!")
print('\n1.Square\n2.Rectangle\n3.Triangle\n4.Circle')
val = int(input('\nchoose the shape you want to find the area for:'))
if val == 1:
  s = int(input("side:"))
  sq = s*s
  print('Area of square is ')
  print(sq)
elif val == 2:
  l= int(input('length:'))
  w= int(input('width:'))
  rect = l*w
  print('Area of rectangle is')
  print(rect)
elif val == 3:
  base = int(input('base:'))
  h = int(input('height:'))
  Triangle = 0.5*base*h
  print('Area of triangle is')
  print(Triangle)
elif val == 4:
  r = int(input('radius:'))
  circle = 3.14 *r*r
  print('Area of circle is')
  print (circle)
else:
  print('wrong choice.')