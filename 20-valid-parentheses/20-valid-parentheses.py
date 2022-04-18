class Solution:
    def isValid(self, s: str) -> bool:
        accepted_pairs = ["()", "[]", "{}"]
        while True:
            for pair in accepted_pairs:
                if pair in s:
                    s = s.replace(pair, '')
            if len(s) == 0:
                return True
            if not any(pair in s for pair in accepted_pairs):
                return False