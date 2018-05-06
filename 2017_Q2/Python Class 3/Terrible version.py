x = 'Number of cows: 45'

#Terrible version
fin = []
x = list(x)

if x[len(x)-1] != ' ':   #If there's no space at the end,
    x.append(' ')        #it won't recognize the last "word."

prev = 0
for i,y in enumerate(x): #Enumerate: iterate over the indexes and values
    if y == ' ':
        fin.append(''.join(x[prev:i]))
        prev = i + 1

print(fin)
