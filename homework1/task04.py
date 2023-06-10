"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
def check_sum_of_four(a: list[int], b: list[int], c: list[int], d: list[int]) -> int:
    
    result = []
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if (a[i]+b[j]+c[k]+d[l]==0):
                        result.append([i,j,k,l])
    return result