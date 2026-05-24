class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        myFreq = {}

        for ss in s:
            myFreq[ss] = myFreq.get(ss, 0) + 1
        for tt in t:
            myFreq[tt] = myFreq.get(tt, 0) -1

        for val in myFreq.values():
            if val != 0:
                return False
        return True