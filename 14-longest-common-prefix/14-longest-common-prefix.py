class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        # Empty List
        if len(strs) == 0:
            return prefix

        # Single item list
        if len(strs) == 1:
            return strs[0]

        # Sort list so we are using the shortest word
        strs_sorted = sorted(strs, key=len)
        shortest_word = strs_sorted[0]
        words = strs_sorted[1:]

        # Spent wayyyy too much time on trying to do this until a discovered all() - <3 Python
        for index in range(len(shortest_word)):
            if not all(shortest_word[index] == word[index] for word in words):
                break
            else:
                prefix = prefix + shortest_word[index]
        return prefix
