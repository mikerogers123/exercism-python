def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return personal_top_n(3)(scores)

def personal_top_n(n):
    return lambda scores: sort(scores)[:n]

def sort(l):
     l.sort(reverse=True)
     return l
    
