x = input().split()
h1 = int(x[0])
m1 = int(x[1])
h2 = int(x[2])
m2 = int(x[3])
if m1>m2:
    m2 = m2+60
    h2 = h2-1
m3 = m2-m1
h3 = h2-h1
print(h3,end=' ')
print(m3)
