# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.


## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    vd = {}
    for sen in strlist:
        strsen = sen.split()
        sen_vote_list = []
        for vote in strsen[3:]:
            sen_vote_list.append(int(vote))
        vd[strsen[0]] = sen_vote_list
    return vd


## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum([x*y for (x,y) in zip(voting_dict[sen_a], voting_dict[sen_b])])


## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """
    similar_factor = -1000
    similar_sen = ""
    for compare_sen in voting_dict.keys():
        compare = policy_compare(sen, compare_sen, voting_dict)
        if compare > similar_factor:
            if sen != compare_sen:
                similar_factor = compare
                similar_sen = compare_sen
    return similar_sen


## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
        >>> least_similar('c', vd)
        'b'
    """
    similar_factor = 1000
    similar_sen = ""
    for compare_sen in voting_dict.keys():
        compare = policy_compare(sen, compare_sen, voting_dict)
        if compare < similar_factor:
            if sen != compare_sen:
                similar_factor = compare
                similar_sen = compare_sen
    return similar_sen


## 5: (Task 2.12.5) Chafee, Santorum
most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 


# (Task 2.12.6) How similar are the voting records of the two senators from 
# your state? Hutchison, Cornyn: 42


## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    return (sum([policy_compare(sen, sen_set_i, voting_dict) for sen_set_i in 
            sen_set])/len(sen_set))

"""
import politics_lab
f = open('voting_record_dump109.txt')
mylist = list(f)
vd = politics_lab.create_voting_dict(mylist)
demset = {list_elem.split()[0] for list_elem in mylist if list_elem.split()[1] == 'D'}
demlist = []
for list_elem in mylist:
    split_list_elem = list_elem.split()
    if split_list_elem[1] == 'D':
        demlist.append(split_list_elem[0])
similar_factor = -1000
for dem_sen in demlist:
    dem_sen_factor = politics_lab.find_average_similarity(dem_sen, demlist, vd)
    if dem_sen_factor > similar_factor:
        similar_factor = dem_sen_factor
        similar_sen = dem_sen
print('Most average democrat = %s' similar_sen)
"""
# most_average_Democrat = 'Biden'


## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    avg_vote = [0.0] * len(voting_dict[list(voting_dict.keys())[0]])
    for sen in sen_set:
        for i in range(len(voting_dict[sen])):
            avg_vote[i] = avg_vote[i] + voting_dict[sen][i]/len(sen_set)
    return avg_vote

average_Democrat_record = [-0.16279069767441862, -0.2325581395348837, 1.0000000000000007, 0.8372093023255818, 0.9767441860465123, -0.13953488372093023, -0.9534883720930238, 0.8139534883720934, 0.9767441860465123, 0.9767441860465123, 0.906976744186047, 0.7674418604651165, 0.6744186046511629, 0.9767441860465123, -0.511627906976744, 0.9302325581395354, 0.9534883720930238, 0.9767441860465123, -0.3953488372093022, 0.9767441860465123, 1.0000000000000007, 1.0000000000000007, 1.0000000000000007, 0.9534883720930238, -0.4883720930232556, 1.0000000000000007, -0.3255813953488371, -0.06976744186046509, 0.9767441860465123, 0.8604651162790702, 0.9767441860465123, 0.9767441860465123, 1.0000000000000007, 1.0000000000000007, 0.9767441860465123, -0.3488372093023255, 0.9767441860465123, -0.4883720930232556, 0.2325581395348837, 0.8837209302325586, 0.4418604651162789, 0.906976744186047, -0.906976744186047, 1.0000000000000007, 0.906976744186047, -0.30232558139534876]


## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    # For each senator, find least similar
    # If similar factor is greater than current similar factor, set
    rival_factor = 0
    for sen_a in voting_dict.keys():
        for sen_b in voting_dict.keys():
            sen_compare = policy_compare(sen_a, sen_b, voting_dict)
            if sen_compare < rival_factor:
                rival_factor = sen_compare
                rivals = (sen_a, sen_b)
    return rivals