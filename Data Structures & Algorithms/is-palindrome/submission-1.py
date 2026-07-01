class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowered = s.lower()
        
        left = 0
        right = len(lowered) - 1

        while left < right:
            if not lowered[left].isalnum():
                left += 1
                continue
            if not lowered[right].isalnum():
                right -= 1
                continue
            if lowered[left] != lowered[right]:
                return False
            left += 1
            right -= 1
        return True