class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        if num_string == num_string[::-1]:
            return True
        return False