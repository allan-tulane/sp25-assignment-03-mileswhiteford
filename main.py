import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED=None):
    if MED is None:
        MED = {}
    if (S, T) in MED:
        return MED[(S, T)]
    if (S == ""):
        MED[(S, T)] = len(T)
    elif (T == ""):
        MED[(S, T)] = len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED) + 1
        delete = fast_MED(S[1:], T, MED) + 1
        MED[(S, T)] = min(insert, delete)
    return MED[(S, T)]
    
def fast_align_MED(S, T, MED=None):
    if MED is None:
        MED = {}
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        alignment_S = '-' * len(T)
        alignment_T = T
        MED[(S, T)] = (len(T), alignment_S, alignment_T)
        return (len(T), alignment_S, alignment_T)
    elif T == "":
        alignment_S = S
        alignment_T = '-' * len(S)
        MED[(S, T)] = (len(S), alignment_S, alignment_T)
        return (len(S), alignment_S, alignment_T)
    else:
        if S[0] == T[0]:
            dist, align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
            result = (dist, S[0] + align_S, T[0] + align_T)
        else:
            dist_ins, align_S_ins, align_T_ins = fast_align_MED(S, T[1:], MED)
            dist_del, align_S_del, align_T_del = fast_align_MED(S[1:], T, MED)

            if dist_ins <= dist_del:
                result = (1 + dist_ins, '-' + align_S_ins, T[0] + align_T_ins)
            else:
                result = (1 + dist_del, S[0] + align_S_del, '-' + align_T_del)

        MED[(S, T)] = result
        return result

