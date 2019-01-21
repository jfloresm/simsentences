from timeit import default_timer as timer
from collections import defaultdict
from itertools import product
from itertools import combinations

d=defaultdict(set)

filename = raw_input("Please enter the name of the file with the sentences (include file type, ex: .txt): ")
fname = raw_input("Please enter the name you want for the output file (with deleted similar) sentences. Include file type (ex: .txt): ")

start = timer()

with open(filename) as f:
    for item in f.readlines():
        d[len(item.split())].add(item.strip()) #creates a dictionary with keys being the lengths of the sentences and values being a set with all sentences of a given length


r = d.keys()
#print r

#This part of the code came from Xiu Khun, I just corrected a few typos
########################################################################
def amam(set_sentences, nwords):
    """ 
    Given a set of sentences in the form of word tuples, remove all 'duplicate'
    tuples. One tuple is duplicate with another if they contain a same nwords
    subtuple.  
    
    INPUT:  set_tuples  a set of tuples with same length
            nwords      length of subtuple to determine 'duplicativeness'
    OUTPUT: None
    """
    if set_sentences == set():
        return None
    if nwords <= 0:
        x = set_sentences.pop()
        set_sentences.clear()
        set_sentences.add(x)
        return None
    s = set()
    news = set()
    to_remove = set()
    for t in set_sentences:
        for st in combinations(t.split(), nwords):             
	    if st in s:
                to_remove.add(t)
                news.clear()
                break
	    else:
                news.add(st)
	#	print(st)
        s.update(news)
#	print(s)
        news.clear()
   # print(to_remove)
    set_sentences -= to_remove
    return None
######################################################################

for key, set_sentences in d.items():
    amam(set_sentences, key-1)


#My Code which was taking too much memory.
###############################################################
#for j in range(len(d.keys())-1,-1,-1):
#	if r[j] == 0:
#		break
#        to_remove = set()
#	for s in d[r[j]]:
#		for x in combinations(s.split(), r[j]-1):
#		#	print(x)
#			if x in d1:
#				to_remove.add(s)
#                                break;
#			else: d2[x].add(s)
#                d1.update(d2)
#                d2.clear()
#        d[r[j]] -= to_remove
#        to_remove.clear()
#        d1.clear()
#############################################################

for j in range(len(r)-1,-1,-1):
	if d.keys()[j]-2 == d.keys()[j-2]:
                for k in d[r[j]]:	
			s = k.split()
			l = len(s)
                        for y in combinations(s,l-2):
				l2 = ' '.join(y)
				
				d[r[j-2]].discard(l2)

	elif d.keys()[j]-2 == d.keys()[j-1]:
		for k in d[r[j]]:
                        s = k.split()
                        l = len(s)
                        for y in combinations(s,l-2):
                                l2 = ' '.join(y)
                                d[r[j-1]].discard(l2)




	
end = timer()
print end - start, 'seconds.'

cout = 0
for j in range(len(r)-1,-1,-1):
        cout += len(d[r[j]])

print cout, 'output lines.'

file = open(fname,mode='w')

for j in range(len(r)-1,-1,-1):
        for item in d[r[j]]:
                file.write("%s\n" %item)

file.close()

