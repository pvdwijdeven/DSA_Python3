def todec(c,a):
  b = list(a)
  s = 0
  x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
  for pos, digit in enumerate(b[-1::-1]):
      y = x.index(digit)
      if int(y)/c >= 1:
          print('Invalid input!!!')
          break
      s = (int(y) * (c**pos)) + s
  return (s)
  

print(todec(7,"353"))
