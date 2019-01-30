import sys
from collections import deque

def balanced(parens):
    left_stack = deque()

    for i in range(len(parens)):
        if parens[i] == '(':
            left_stack.append(parens[i])
        else:
            if len(left_stack) > 0:
                left_stack.pop()
            else:
                return(i)

    return(True)


def valid_input(input_str):
    if len(input_str) == 0:
        return(False)

    for letter in input_str:
        if not (letter == '(' or letter == ')'):
            return(False)

    return(True)

if __name__ == '__main__':
    parentheses = sys.stdin.read()

    assert valid_input(parentheses)

    print(balanced(parentheses))
