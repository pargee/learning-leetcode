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

        # Check for sub values first
        for key, value in sub_values.items():
            if key in s:
                print(key)
                print(value)
                num = num + value
                s = s.replace(key, '')

        # Make a list from the remaining chars
        for val in s:
            num = num + values[val]

        return num