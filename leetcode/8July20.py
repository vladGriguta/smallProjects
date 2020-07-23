class Solution:
    def threeSum(self, nums):       
        # array with results
        results = []

        # sort our array for simplicity:
        nums = sorted(nums)

        
        # fix the first number
        for i_x in range(len(nums)):
            
            # if already considered the current x value continue to the next one
            if((i_x>0) and (nums[i_x]==nums[i_x-1])):
                continue
            
            # this is the value that needs to be matched by the sum of the other two variables
            value = -nums[i_x]


            # select the indices of the first (smallest) and last (largest) elements in the remaining array
            start_idx = i_x + 1
            end_idx = len(nums) - 1

            # iterate through pairs of elements
            while start_idx<end_idx:
            	# compute the sum of the current elements
                s = nums[start_idx] + nums[end_idx]

                # if the sum of the two number is larger than the fixed number (x), then we need to decrement the sum
                # by taking the next smaller number from the end (remember, the array is sorted)
                if s > value:
                    end_idx -= 1
                # same goes if the sum is smaller, only this time we need to increment the lower number 
                # (the one on theleft of the sorted array)
                elif s < value:
                    start_idx += 1

                # else, we found a new solution
                else:
                    x = nums[i_x]
                    y = nums[start_idx]
                    z = nums[end_idx]
                    results.append([x,y,z])

                    # if duplicate solutions are found, ignore them:
                    while((start_idx<end_idx) and (nums[start_idx]==y)):
                        start_idx = start_idx + 1
                    while((start_idx<end_idx) and (nums[end_idx]==z)):
                        end_idx = end_idx - 1

        return results