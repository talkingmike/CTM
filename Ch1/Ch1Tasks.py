from plotting import plot

# Task 1.4.1
S={2+2j,3+2j,1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
plot(S,4)


# Task 1.4.3
plot({1+2j+z for z in S},4)


# Quiz 1.4.4: For what value of z0 does the translation f(z) = z0 + z move the 
# left eye to the origin?
plot({-2-2j+z for z in S},4)


# Problem 1.4.5: Show that, for any two distinct points z1 and z2:
# * there is a translation that maps z1 to z2
# * there is a translation that maps z2 to z1, and
# * there is no translation that both maps z2 to z1 and z1 to z2
'''
z1 = a+bj
z2 = c+cj

z1 + X1 = z2
X1 = z2 - z1
X1 = (c-a)+(c-b)j


z2 + X2 = z1
X2 = z1 - z2
X2= (a-c)+(b-c)j

X1 != X2
'''


# Problem 1.4.6: Draw adiagram representing the complex number z0 = -3+3j using 
# two arrows with their tails at different points.
'''
This would be a drawing of a vector <-3,3> with the endpoint at two different 
points. For example one at (0,0), another at (1,1)
'''


# Task 1.4.7: Create a new plot title "My Scaled Points" using a comprehension
# as in Task 1.4.3. The points in the new plot should be halves of the points 
# in S.
plot({0.5*z for z in S}, 4)


# Task 1.4.8: Create a new plot in which the points of S are rotated by 90 
# degrees and scaled by 1/2. Use a comprehension in which the points of S are 
# multipled by a single complex number.
plot({0.5j*z for z in S},4)



# Task 1.4.9: Using a comprehension, create a new plot in which the points of 
# S are rotated by 90 degrees, scaled by 1/2, and then shifted down by one 
# unit and to the right two units. Use a comprehension in which the points of S
# are multiple by one complex number and added to another.
plot({0.5j*z+2-1j for z in S},4)


# Task 1.4.10: *Import test image using provided procedure.* Use a 
# comprehension to assign to a list pts the set of complex numbers x+yi such 
# that the image intensity of pixel (x,y) is less than 120, and plot the list 
# pts.
import image
data = image.file2image('img01.png')
bw_data = image.color2gray(data)

'''
    Keep these in mind:
    Something to do with this statement: [[x for x in row] for row in image]
    
    S={2+2j,3+2j,1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
    plot(S,4)

    Use enumerate(List) to return a tuple of (index,List(item))
'''

pts = [complex(col_ind,row_ind) for (row_ind,row) in enumerate(bw_data) for 
       (col_ind,intensity) in enumerate(row) if intensity < 120]

plot({-1j*z+189j for z in pts}, 200, 1)
