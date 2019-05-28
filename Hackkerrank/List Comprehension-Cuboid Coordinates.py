#x,y and z representing the dimensions of a cuboid along with an integer n.
#print a list of all possible coordinates given by (i,j,k) on a 3D grid
#where the sum of i+j+k is not equal to n.
#print the list in lexicographic increasing order.
x,y,z,n = (int(input()) for _ in range(4))
coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(coordinates)