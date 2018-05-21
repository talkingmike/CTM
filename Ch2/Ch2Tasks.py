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


# Quiz 2.9.4: list_dot(u, v)
def list_dot(u, v):
    return sum([a*b for (a,b) in zip(u, v)])


# Quiz 2.9.15: dot_product_list(needle,haystack)
def dot_product_list(needle, haystack):
    needle_len = len(needle)
    return [list_dot(needle, haystack[i:i+needle_len]) for i in range(
        len(haystack) - needle_len)]


# Quiz 2.10.1: list2vec(L)
def list2vec(L):
    return Vec(set(range(len(L))), {k:x for (k,x) in enumerate(L)})
# Provided in module in vecutil.py


# Exercise 2.11.4: Enter triangular_solve_n into Python and try it out on the 
# example system above.
def triangular_solve_n(rowlist, b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x

# I don't think my Vec library is complete yet; the loop tries to reference an 
# element of rowlist and subtract from an element of b, but rowlist elements 
# are Vec objects... Does the complete Vec implementation have some kind of 
# polymorphic function that will return a value when reference a Vec element?