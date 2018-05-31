# Also solves pe_67 because it's good

# Standard data imports
with open('p067_triangle.txt','r') as f:
    seed = f.readlines()
mod = [[int(y) for y in x.split(' ')] for x in seed]

# Here's the clever solution
# Work from the bottom up
sums = [x for x in mod[-1]] # First I create the sums list at the very bottom
for row_num,row in enumerate(mod[:-1][::-1]): 
    # Now for each step in the triangle, I create a new sums list which adds the maximum lower element
    sums = [max(x+sums[i],x+sums[i+1]) for i,x in enumerate(row)]
# When done, this corresponds to the top element of the triangle (or maximum path sum)
print(sums)
