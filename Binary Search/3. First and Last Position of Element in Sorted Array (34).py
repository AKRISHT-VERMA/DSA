class Solution:
    def firstOccurrence(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        firstposition = -1
        while (low <= high):
            mid = (low + high)//2
            if nums[mid] < target :
                low = mid + 1

            elif nums[mid] > target :
                high = mid - 1

            else:
                firstposition = mid
                high = mid - 1

        return firstposition        
    
    def lastOccurrence(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        lastposition = -1
        while (low <= high):
            mid = (low + high)//2
            if nums[mid] < target :
                low = mid + 1

            elif nums[mid] > target :
                high = mid - 1

            else:
                lastposition = mid
                low = mid + 1

        return lastposition  
    
    def searchRange(self, nums: list[int], target: int) -> list[int] :
        first = self.firstOccurrence(nums, target)
        last = self.lastOccurrence(nums, target)

        return [first, last]
    
        
if __name__ == "__main__":
    sol = Solution()

    print(sol.searchRange([5,7,7,8,8,10], 8)) 
    print(sol.searchRange([5,7,7,8,8,10], 6))   
    print(sol.searchRange([], 1))               
    print(sol.searchRange([1], 1))            
    print(sol.searchRange([1], 2))              
    print(sol.searchRange([2,2], 2))          
    print(sol.searchRange([2,2,2,2,2], 2))    
    print(sol.searchRange([1,2,3,4,5], 1))    
    print(sol.searchRange([1,2,3,4,5], 5))    
    print(sol.searchRange([1,2,2,2,3,4], 2))  
    print(sol.searchRange([1,1,2,3,4], 1))    
    print(sol.searchRange([1,2,3,4,5,5], 5))  
    print(sol.searchRange([8,8,8,8,8,8,8], 8))        


