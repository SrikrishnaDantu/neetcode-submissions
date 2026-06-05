class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char in my_dict:
                if stack and stack[-1] == my_dict[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return True if len(stack) == 0 else False