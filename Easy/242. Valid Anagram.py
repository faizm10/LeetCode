class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare
        return sorted(s) == sorted(t)
    
# Main function to test the isAnagram method
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    
    # Check if s1 and t1 are anagrams
    result1 = solution.isAnagram(s1, t1)
    print(f"'{s1}' and '{t1}' are anagrams: {result1}")  # Expected output: True
    
    # Check if s2 and t2 are anagrams
    result2 = solution.isAnagram(s2, t2)
    print(f"'{s2}' and '{t2}' are anagrams: {result2}")  # Expected output: False
