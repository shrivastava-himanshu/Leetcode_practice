class Solution:
    def isValid(inp_str: str) -> bool:
        if not inp_str or len(inp_str) == 0:
            return True

        stack = []
        for i in inp_str:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and (len(stack) == 0 or stack[-1] != '('):
                return False
            elif i == '}' and (len(stack) == 0 or stack[-1] != '{'):
                return False
            elif i == ']' and (len(stack) == 0 or stack[-1] != '['):
                return False
            else:
                stack.pop()

        if len(stack) > 0:
            return False
        return True



    if __name__ == '__main__':
        str = ["(])","()","()[]{}","(]","([)]","{[]}"]

        for i in str:
            print(isValid(i))