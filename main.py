import random
x = random.randrange(1, 100, 1)
#print(x)
a = random.randrange(1, 9, 1)
b = random.randrange(1, 9, 1)
c = random.randrange(1, 9, 1)
d = random.randrange(1, 9, 1)
e = random.randrange(1, 9, 1)
f = random.randrange(1, 9, 1)
while a == b or c or d or e or f:
  a = random.randrange(1, 9, 1)
  if a != b or c or d or e or f:
    break
while b != a or c or d or e or f:
  b = random.randrange(1, 9, 1)
  if b != a or c or d or e or f:
    break
while c == a or b or d or e or f:
  c = random.randrange(1, 9, 1)
  if c != a or b or d or e or f:
    break
while d == a or b or c or e or f:
  d = random.randrange(1, 9, 1)
  if d != b or c or d or e or f:
    break
while e == a or b or c or d or f:
  e = random.randrange(1, 9, 1)
  if e != b or c or d or e or f:
    break
while f == a or  b or c or d or e:
  a = random.randrange(1, 9, 1)
  if a != b or c or d or e or f:
    break
#f = 9
z = [a, b, c, d, e, f]
y = sorted(z) 
dum = 3
#while dum == 3:
#  print(y)
while z != y:
  if a > b:
    al = a
    bl = b
    b = al
    a = bl
    bl = b
    al = a
  if b > c:
    bl = b
    cl = c
    b = cl
    c = bl
    cl = c
  if c > d:
    cl = c
    dl = d
    c = dl
    d = cl
    dl = d
  if d > e:
    dl = d
    el = e
    d = el
    e = dl
    el = e
  if e > f:
    el = e
    fl = f
    e = fl
    f = el
    fl = f
  z = [a, b, c, d, e, f]
  print(z)
  if z == y:
    break
print("yay")