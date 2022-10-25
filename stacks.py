#stack - easy
#need hashmap 
from turtle import back


def isValid(s):
    stack = []
    closeToOpen = { ")" : "(", "]" : "[",  "}" : "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
print(isValid("())("))


#155 Min Stack - EASY
#push, pop, top and getMin
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]

#generate parentheses
class solution:
    def genpar(self, n):
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                

#monotonic decreasing stack
#increasing temps
class sol:
    def dailyTemp(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


#car fleet
# n cars traveling, a single lane
#      



