class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        s_new_withoutalpha = ''
        for i in s_new:
            if i.isalnum():
                s_new_withoutalpha+= i
        print(s_new_withoutalpha)
        return s_new_withoutalpha == s_new_withoutalpha[::-1]


        