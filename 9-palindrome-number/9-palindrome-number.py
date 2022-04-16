class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the numbers to a string then reverse it (should be faster than a list?)
        num_string = str(x)
        if num_string == num_string[::-1]:
            return True
        return False