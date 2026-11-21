class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        # for key,value in freq.items():
        #     a=freq.keys(max(freq.value()))
        top=max(freq,key=freq.get)
        print(top)
        
       
        return top

        