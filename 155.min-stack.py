# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, val: int) -> None:
        # Let self.mins[i] be min(self.values[0:i+1]).
        # This means, that
        #   self.mins[i-1] == min(self.values[0:i])
        # and thus,
        #   self.mins[i] = min(self.mins[i-1], self.values[i])

        m = val
        if self.mins:
            m = min(val, self.mins[-1])
        
        self.values.append(val)
        self.mins.append(m)
        
    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.values[-1]       

    def getMin(self) -> int:
        return self.mins[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()