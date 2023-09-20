fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for mm in fh :
    if not mm.startswith('From'): continue
    if mm.startswith('From:'): continue
    count=count+1
    ww=mm.split()
    print(ww[1])
    
    

print("There were", count, "lines in the file with From as the first word")
