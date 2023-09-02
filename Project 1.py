doc = open("document.txt","r")

c=[]

for x in doc:
  c.append(x.split(' '))
  print(c)

d=0

for i in range(len(c)):
  d=d+1

print(d)