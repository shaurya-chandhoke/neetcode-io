class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = [char.lower() for char in s if char.isalnum()]
        print(cleaned_str)
        return cleaned_str == cleaned_str[::-1]