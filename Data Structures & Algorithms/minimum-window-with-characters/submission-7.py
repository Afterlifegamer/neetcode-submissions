from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required = Counter(t)  # Tracks required chars with frequency
        window = defaultdict(int)
        have, need = 0, len(required)

        res = ""
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            if char in required:
                window[char] += 1
                if window[char] == required[char]:
                    have += 1

            # Try to shrink the window from left
            while have == need:
                # Save the result if it's smaller
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                # Pop from left of window
                if s[l] in required:
                    window[s[l]] -= 1
                    if window[s[l]] < required[s[l]]:
                        have -= 1
                l += 1

        return res
