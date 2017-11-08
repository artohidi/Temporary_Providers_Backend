import numpy

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split(" "))))
n_1 = numpy.array(s)
print (numpy.prod(n_1))