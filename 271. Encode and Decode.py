class Solution:

    def encode(self, strs: List[str]) -> str:
        return "#".join(strs)       # 'a,b,c'


    def decode(self, s: str) -> List[str]:
        return s.split("#") 