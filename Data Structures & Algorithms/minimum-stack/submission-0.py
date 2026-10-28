class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        length=len(self.stack)
        return self.stack[length-1]

        

    def getMin(self) -> int:
        sorted_list = sorted(self.stack)
        return sorted_list[0]
        
