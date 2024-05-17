class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}
        mydict1={}
        if len(s) != len(t):
            return False
        for char in s:
            if char in mydict:
                mydict[char]+=1
            else:
                mydict[char]=1
        for char in t:
            if char in mydict1:
                mydict1[char] += 1
            else:
                mydict1[char] = 1
        for x in mydict:
            if mydict.get(x, 0) != mydict1.get(x, 0):
                return False
        return True