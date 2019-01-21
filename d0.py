from timeit import default_timer as timer

filename = raw_input("Please enter the name of the file with the sentences (include file type, ex: .txt): ")
fname = raw_input("Please enter the name you want for the output file (with deleted similar) sentences. Include file type (ex: .txt): ")


start = timer()

with open(filename) as f:
        s1 =set((f.readlines())) #read lines as sets

end = timer()

time = (end - start)

print(time)

cout = 0
for j in range(0, len(s1)):
        cout += 1

print cout


file = open(fname,mode='w')

for item in s1:
	file.write("%s\n" %item)

file.close()

