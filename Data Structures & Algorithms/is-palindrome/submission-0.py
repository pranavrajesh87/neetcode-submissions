class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str=""
        for char in s:
            if char.isalnum():
                cleaned_str+=char.lower()
        reversed_str=cleaned_str[::-1]
        return cleaned_str == reversed_str           