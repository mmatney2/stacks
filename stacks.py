#stack - easy
#need hashmap 
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




