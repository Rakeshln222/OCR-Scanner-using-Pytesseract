# utils.py
def cer(ref, hyp):
    # character error rate (Levenshtein)
    import numpy as np
    r, h = list(ref), list(hyp)
    d = np.zeros((len(r)+1, len(h)+1), dtype=int)
    for i in range(len(r)+1): d[i,0]=i
    for j in range(len(h)+1): d[0,j]=j
    for i in range(1,len(r)+1):
        for j in range(1,len(h)+1):
            cost = 0 if r[i-1]==h[j-1] else 1
            d[i,j] = min(d[i-1,j]+1, d[i,j-1]+1, d[i-1,j-1]+cost)
    return d[len(r), len(h)] / max(1, len(r))

# usage:
# print("CER:", cer(ground_truth_text, extracted_text))
