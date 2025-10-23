class Solution:
    def isValid(self, s: str) -> bool:
        combinations = { ")" : "(", "]" : "[", "}" : "{" }
        result = []
        for c in s:
            if c in combinations: 
                if result and result[-1] == combinations[c]: 
                    # checks if top of the stack matches the closing bracket
                    result.pop()
                else:
                    #pushes the closing bracket 
                    return False
            else:
                result.append(c)
        return True if not result else False

