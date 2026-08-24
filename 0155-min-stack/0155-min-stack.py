class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, value):
        self.stack.append(value)
        if not self.minstack or value<= self.minstack[-1]:
            self.minstack.append(value)
        

    def pop(self):
        value = self.stack.pop()
        if value == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()