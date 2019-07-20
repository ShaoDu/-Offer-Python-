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



