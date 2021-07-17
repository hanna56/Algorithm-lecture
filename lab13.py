# 후위표현 수식 계산
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while not opStack.isEmpty():
                pop_token = opStack.pop()
                if pop_token == '(':
                    break
                postfixList.append(pop_token)
        else:
            while not opStack.isEmpty():
                if prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
                else:
                    break
            opStack.push(token)
            
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
            continue
        
        token1 = valStack.pop()
        token2 = valStack.pop()
        
        if token == '+':
            valStack.push(token2 + token1)
        elif token == '-':
            valStack.push(token2 - token1)
        elif token == '*':
            valStack.push(token2 * token1)
        elif token == '/':
            valStack.push(token2 / token1)
    
    return valStack.pop()
        


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
