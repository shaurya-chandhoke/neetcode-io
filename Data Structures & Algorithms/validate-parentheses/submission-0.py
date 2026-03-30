class Solution:
    def isValid(self, s: str) -> bool:
        lookup_table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char not in lookup_table:
                stack.append(char)
                continue
            
            if not stack or stack.pop() != lookup_table[char]:
                return False
        
        return len(stack) == 0