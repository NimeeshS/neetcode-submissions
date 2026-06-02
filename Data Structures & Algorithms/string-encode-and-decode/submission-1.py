class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "elephant"
        return "secretencoder".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "elephant": return []
        return s.split("secretencoder")