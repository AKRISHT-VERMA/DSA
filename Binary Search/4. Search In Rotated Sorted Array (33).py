class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high :
            mid = (low + high)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1    

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1                                 
        
if __name__ == "__main__":
    sol = Solution()

    print(sol.search([4,5,6,7,0,1,2], 0))  
    print(sol.search([4,5,6,7,0,1,2], 3))    
    print(sol.search([1], 0))                
    print(sol.search([1], 1))               
    print(sol.search([3,1], 1))             
    print(sol.search([3,1], 3))             
    print(sol.search([5,1,3], 5))           
    print(sol.search([5,1,3], 1))           
    print(sol.search([5,1,3], 3))           
    print(sol.search([6,7,8,1,2,3,4,5], 2)) 
    print(sol.search([6,7,8,1,2,3,4,5], 7)) 
    print(sol.search([6,7,8,1,2,3,4,5], 5)) 
    print(sol.search([6,7,8,1,2,3,4,5], 9))          