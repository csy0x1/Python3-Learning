'''
搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0


class Solution:
    def searchInsert(self, nums, target):
        for i,j in enumerate(nums):
            if j==target:
                print(i)
                print(nums)
                return i
            elif target>j and i==len(nums)-1:
                print(i+1)
                nums.insert(i+1,target)
                print(nums)
                return i
            elif j>target:
                print(i)
                nums.insert(i,target)
                print(nums)
                return i
            


test=Solution()
test.searchInsert([1,3,5,6],7)
'''

#二分查找法:
class Solution:
    def searchInsert(self, nums, target):
        n=len(nums)
        left=0
        right=n-1
        ans=n
        while(left<=right):   
            mid=int((left+right)/2)
            if target<=nums[mid]:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        print(ans)
        return ans

test=Solution()
test.searchInsert([1,3,5,6],7)
'''
二分查找不应使用for循环遍历列表
错误：
--snip--
        for i,j in enumerate(nums):
            mid=int((left+right)/2)
            if target<=j:
                ans=i
                right=mid-1
            else:
                left=mid+1
        return ans
'''

