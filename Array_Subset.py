#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        ca, cb = Counter(a), Counter(b)
        for key in cb:
            if cb[key] > ca[key]:
                return False
        return True