class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        j=0
        k=0
        for i in range(2,len(nums)):
            if arr1[j]>arr2[k]:
                arr1.append(nums[i])
                j=j+1
            else:
                arr2.append(nums[i])
                k=k+1
        arr1.extend(arr2)
        return arr1
        