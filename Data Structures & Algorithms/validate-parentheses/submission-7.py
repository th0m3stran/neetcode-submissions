class Solution:
    def isValid(self, s: str) -> bool:

        pairs = { #mapping every closing bracket to opening bracket
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for char in s:
            if char in "([{": #if opening paranthesis 
                stack.append(char)
            else: #closing bracket 
                if not stack:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

        return not stack




        