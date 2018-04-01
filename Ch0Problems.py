## (Problem 0.8.1) Increments
def increments(L): return [i+1 for i in L]

## (Problem 0.8.2) Cubes
def cubes(L): return [i**3 for i in L]

## (Problem 0.8.10)
'''
    f(x) = x+1 on domain {1,2,3,5,6}
    Pr(1) = 0.5
    Pr(2) = 0.2
    Pr(3) = 0.1
    Pr(5) = 0.1
    Pr(6) = 0.1

    Probability of getting even? 0.5 + 0.1 + 0.1
    Probability of getting odd? 0.2 + 0.1
'''

## (Problem 0.8.11)
'''
    g(x) = x mod 3 on domain {1,2,3,4,5,6,7}, codomain {0,1,2}
    g(1) = 1
    g(2) = 2
    g(3) = 0 
    g(4) = 1
    g(5) = 2
    g(6) = 0
    g(7) = 1
    Pr(1) = 0.2
    Pr(2) = 0.2
    Pr(3) = 0.2
    Pr(4) = 0.1
    Pr(5) = 0.1
    Pr(6) = 0.1
    Pr(7) = 0.1

    Probability of g(x) = 1? 0.2 + 0.1 + 0.1 = 0.4
    Probability of g(x) = 0 or 2? 0.2 + 0.2 + 0.1 + 0.1 = 0.6
'''