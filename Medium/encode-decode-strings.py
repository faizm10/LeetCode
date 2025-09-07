class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            length = int(s[i:j])  # parse length
            j += 1                # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res