from math import log2
import time

# returns the entropy for given list of probabilities
def entropy(prob):
    return sum(-p*log2(p) for p in prob if p > 0)

# returns the average code length for given probabilities
def avgLength(code, prob):
    assert(code.keys() == prob.keys())
    return sum(prob[k] * len(code[k]) for k in prob.keys())

# returns the efficiency of the coding scheme
def efficiency(ent, avglen):
    return ent/avglen

def rand(a,b):
    dt= int(round(time.time()))
    return (dt%b)+a