from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        letters = sorted(freq.keys())
        result = []

        def attempt(pos, freq, tight):
            if pos == n:
                candidate = "".join(result)
                return candidate if candidate > target else ""

            for ch in letters:
                if freq[ch] == 0:
                    continue
                if tight and ch < target[pos]:
                    continue

                # choose ch
                result.append(ch)
                freq[ch] -= 1

                if not tight or ch > target[pos]:
                    suffix = []
                    for c in letters:
                        suffix.extend([c] * freq[c])
                    candidate = "".join(result) + "".join(suffix)
                    if candidate > target:   # strictly greater
                        return candidate

                ans = attempt(pos+1, freq, tight and ch == target[pos])
                if ans:
                    return ans

                # backtrack
                result.pop()
                freq[ch] += 1
            return ""

        return attempt(0, freq, True)
