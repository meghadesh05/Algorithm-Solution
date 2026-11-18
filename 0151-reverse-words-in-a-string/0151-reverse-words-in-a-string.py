class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        res = []
        n = len(word)

        for i in range(n -1, -1, -1):
            res.append(word[i])

            if i != 0:
                res.append(" ")

        return "".join(res)        