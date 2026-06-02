class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        word = ""
        for i in s:
            word += i.lower() if i.lower() in letters else ""

        return word == word[::-1]