class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,

        }
        sub_values = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        sub_list = ["CM", "CD", "XC", "XL", "IX", "IV"]

        # Check for sub values first
        for val in sub_list:
            if val in s:
                num = num + sub_values[val]
                s = s.replace(val, '')

        # Make a list from the remaining chars
        for val in s:
            num = num + values[val]

        return num