# Also solves pe_67 because it's good

with open('p067_triangle.txt','r') as f:
    seed = f.readlines()
mod = [[int(y) for y in x.split(' ')] for x in seed]
# For fun, here's the "pick highest you can see" method
# It obviously won't work in all cases
#soln = 0
#posn = [0,0]
#while posn[1] < len(mod)-1:
#    print(mod[posn[1]][posn[0]])
#    soln += mod[posn[1]][posn[0]]
#    comparisons = mod[posn[1]+1][posn[0]:posn[0]+2]
#    if comparisons[0] > comparisons[1]:
#        posn = [posn[0],posn[1]+1]
#    else:
#        posn = [posn[0]+1,posn[1]+1]
#print(soln)

# Here's the clever solution
# Work from the bottom up
sums = [x for x in mod[-1]]
for row_num,row in enumerate(mod[:-1][::-1]):
    sums = [x+sums[i] if sums[i]>sums[i+1] else x+sums[i+1] for i,x in enumerate(row)]
print(sums)
