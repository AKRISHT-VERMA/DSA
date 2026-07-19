class Solution:
     def findMin(self, nums: list[int]) -> int :
          low = 0
          high = len(nums) - 1
          while low < high:
               mid = (low + high)//2

               if nums[mid] < nums[high]:
                    high = mid

               else:
                    low = mid + 1

          return nums[low]                  


if __name__ == "__main__":
    sol = Solution()

    print(sol.findMin([4,5,6,7,0,1,2]))      
    print(sol.findMin([3,4,5,1,2]))          
    print(sol.findMin([11,13,15,17]))        
    print(sol.findMin([2,1]))                
    print(sol.findMin([1]))                  
    print(sol.findMin([5,1,2,3,4]))          
    print(sol.findMin([2,3,4,5,1]))          
    print(sol.findMin([6,7,8,9,1,2,3,4,5]))  
    print(sol.findMin([7,1,2,3,4,5,6]))      
    print(sol.findMin([1,2,3,4,5,6,7]))                