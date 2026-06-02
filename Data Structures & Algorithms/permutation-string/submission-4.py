class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        m = len(s1)

        # Build first window
        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        # Slide the window
        for r in range(m, len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r - m]) - ord('a')] -= 1

            if window == need:
                return True

        return False