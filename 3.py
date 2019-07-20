题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
运行代码：
def findNums(nums,duplication):
    if len(nums)<=1 or nums==None:
        return False
    for i in range(len(nums)):
        if nums[i]>=len(nums) or nums[i]<0:
            return False
    for i in range(len(nums)):
        while(i!=nums[i]):
            if nums[i]==nums[nums[i]]:
                duplication.append(nums[i])
                break;
            else:
                temp=nums[i]
                nums[i]=nums[temp]
                nums[temp]=temp
        if i==len(nums)-1:
            return duplication
    return None
if __name__=="__main__":
    nums=[2,3,1,0,2,5,3]
    duplication=[]
    s=findNums(nums,duplication)
    print(s)



