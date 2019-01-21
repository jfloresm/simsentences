#import re
from timeit import default_timer as timer
from collections import defaultdict
#from itertools import product
import itertools as it
from itertools import count
from collections import Counter

c = Counter()

filename = raw_input("Please enter the name of the file with the sentences (include file type, ex: .txt): ")
fname = raw_input("Please enter the name you want for the output file (with deleted similar) sentences. Include file type (ex: .txt): ")

start = timer()

d = defaultdict(set)

with open(filename) as f:
    for item in f.readlines():
	x = item.strip()
	c[x] += 1
        d[len(item.split())].add(x)



#Self Explanatory. Only check sentences in keys which are distance 1 apart.

r = d.keys()

for j in range(len(r)-1,-1,-1):
	if d.keys()[j]-1 == d.keys()[j-1]:
		for k in d[r[j]]:
			s = k.split()
			l = len(s)
			for x in it.combinations(s, l-1):
				l2 = ' '.join(x)
				d[r[j-1]].discard(l2)

end = timer()

print(end - start)

cout = 0
for j in range(len(d.keys())-1,-1,-1):
        cout += len(d[r[j]])

print cout

	
file = open(fname,mode='w')

for j in range(len(r)-1,-1,-1):
	for item in d[r[j]]:
		count1 = c[item]
		for x in range(0, c[item]):
        		file.write("%s \n" %item)

file.close()


