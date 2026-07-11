class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True


        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # if we remove one character from the string on either side is it a palindrome?
                return (is_palindrome(left + 1, right) or is_palindrome(left, right - 1))
            else:
                left += 1
                right -= 1
        return True