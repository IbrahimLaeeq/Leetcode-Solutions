class Solution:
    def isPalindrome(self, x: int) -> bool:
       string_x = str(x)
       # typecasting the input from integer data type 
       # to string data - type

       return string_x == string_x[::-1]
       # [::-1] operator reverses the string