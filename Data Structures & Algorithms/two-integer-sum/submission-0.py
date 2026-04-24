class Solution:
    def twoSum(self, nums, target):
        # 1. Create a dictionary to store: {number: index}
        seen = {}
        
        # 2. Loop through the list once
        # 'i' is the index, 'num' is the value
        for i, num in enumerate(nums):
            
            # 3. Calculate what we need to reach the target
            complement = target - num
            
            # 4. Check if we have already seen that complement
            if complement in seen:
                # We found it! Return the stored index and the current index
                return [seen[complement], i]
            
            # 5. If not found, store the current number and its index 
            # so a future number can "find" it
            seen[num] = i

# Create the object
sol = Solution()

# Test with your example
print(sol.twoSum([3, 4, 5, 6], 7)) # Should output [0, 1]            
                    