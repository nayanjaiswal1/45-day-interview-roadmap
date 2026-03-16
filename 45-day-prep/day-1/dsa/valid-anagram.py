class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a') ] += 1
            count[ord(t[i]) - ord('a') ] -= 1

        return all (x == 0 for x in count)
        


# Best for Interviews (Frequency Array)
# isAnagram2 is O(n) time, O(1) space (at most 26 keys for lowercase letters)
