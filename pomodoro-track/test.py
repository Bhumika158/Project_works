class Solution(object):
    def findAnagrams(self, s, p):
        need=0
        need_dict= {}
        index=[]
        for letter in p:
            need+=1
            need_dict[letter]=p.count(letter)
        print(need_dict)
        l=0
        for r in range(2,len(s),2):
            while l<=r and s[l] in need_dict:
                index.append(l)
                l+=1



sol=Solution()
ans=sol.findAnagrams("cbaebabacd","abc")
print(ans)