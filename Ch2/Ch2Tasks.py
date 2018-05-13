from plotting import plot

# Task 2.3.2
L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75,1], [3,1], [3.25,1]]
plot(L, 4)


# Task 2.4.3
def add2(v,w):
    return [v[0]+w[0], v[1]+w[1]]

plot([add2(v,[1,2]) for v in L], 4)


# Quiz 2.4.4: Suppose we represent n-vectors by n-element lists. Write a 
# procedure addn to compute the sum of two vectors so represented.
def addn(v,w):
    return [x+y for (x,y) in zip(v,w)]


# Quiz 2.5.3:  Suppose we represent n-vectors by n-element lists. Write a 
# procedure scalar_vector_mult(alpha, v) that multiplies the vector v by the
# scalar alpha.
def scalar_vector_mult(alpha, v):
    return [alpha*n for n in v]


# Task 2.5.4
plot([scalar_vector_mult(0.5, n) for n in L], 4)
plot([scalar_vector_mult(-0.5, n) for n in L], 4)


# Task 2.6.9
def segment(pt1, pt2):
    diff = addn(scalar_vector_mult(-1,pt1),pt2)
    return [addn(scalar_vector_mult(i/100,diff),pt1) for i in range(101)]
# I don't like this implementation; could this be done simpler with a
# comprehension?


# Quiz 2.7.1: zero_vec(D)
# Provided in zero_vec module in vecutil.py

# Quiz 2.7.2: getitem(v, d)
# Implemented in getitem module in vec.py


# Quiz 2.7.3: scalar_mul(v, alpha)
# Implemented in scalar_mul module in vec.py


# Quiz 2.7.4: add(u, v)
def add(u, v):
    return Vec(u.D,{d:getitem(u,d) + getitem(v,d) for d in u.D})


# Quiz 2.7.5: neg(v)
def neg(v):
    return scalar_mul(v, -1)


# Quiz 2.9.4