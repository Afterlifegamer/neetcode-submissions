class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res1=defaultdict(int)
        res=[]
        
        for index,val in enumerate(nums):
            res1[val]+=1
        sorted_dict_by_value = sorted(res1.items(), key=lambda item: item[1], reverse=True)
        print(sorted_dict_by_value)
        for i in range(k):
            res.append(sorted_dict_by_value[i][0])
            print(res[i])
           
        return res


        