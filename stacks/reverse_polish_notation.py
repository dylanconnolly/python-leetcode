from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            match op:
                case "+":
                    val = stack.pop() + stack.pop()
                    stack.append(val)
                case "-":
                    a, b = stack.pop(), stack.pop()
                    val = b - a
                    stack.append(val)
                case "*":
                    val = stack.pop() * stack.pop()
                    stack.append(val)
                case "/":
                    a, b = stack.pop(), stack.pop()
                    val = int(b / a)
                    stack.append(val)
                case _:
                    stack.append(int(op))

        return stack[-1]


def test(tokens):
    print(Solution().evalRPN(tokens))

test(["2","1","+","3","*"])
test(["4","13","5","/","+"])
test(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])