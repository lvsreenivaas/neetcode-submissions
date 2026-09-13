class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new_token = []
        for token in tokens:
            if token not in ['+','-','*','/'] :
                new_token.append(int(token))
            else:
                b = new_token.pop()
                a = new_token.pop()
                if token == '+':
                    new_token.append(a+b)
                elif token == '-':
                    new_token.append(a-b)
                elif token == '*':
                    new_token.append(a*b)
                elif token == '/':
                    new_token.append(int(a/b))    
        return int(new_token[-1])