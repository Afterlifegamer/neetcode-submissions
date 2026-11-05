class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0 for _ in range(len(temperatures))]
        stack.append(0)
        for i in range(1,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                index=stack.pop()
                output[index]=i-index
            stack.append(i)
        return output






        