# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st
import numpy as np
from scipy import stats

n = int(input())
a = list(map(int,input().split()))

print(st.mean(a))
print(st.median(a))
arr = np.array(a)

m = stats.mode(arr)
print(int(m[0]))
