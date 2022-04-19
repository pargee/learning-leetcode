class Solution:
    def isValid(self, s: str) -> bool:
        st = list()

        # Much cleaner example after doing some research
        for c in s:
            if c == "(" or c == "[" or c == "{":
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                if c == ")" and st[-1] != "(":
                    return False
                if c == "]" and st[-1] != "[":
                    return False
                if c == "}" and st[-1] != "{":
                    return False
                st.pop()
        return len(st) == 0