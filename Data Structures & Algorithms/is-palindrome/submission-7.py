class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()

        left,right = 0, len(lowered) - 1

        while left < right:
            while not lowered[left].isalnum() and left < right:
                left += 1
            while not lowered[right].isalnum() and left < right:
                right -= 1
            if lowered[left] != lowered[right]:
                return False
            left += 1
            right -= 1
        return True