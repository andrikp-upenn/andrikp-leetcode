class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs: list of nums, target: int
        Outputs: [i,j] s.t. i + j target
        """
        # seen numbers in a dict.
        seenNums = {}

        for i in range(len(nums)):
            need_val = target - nums[i] # what number is needed
            if need_val in seenNums:
                # Extract the idx from the num
                j = seenNums[need_val]
                return[j,i]
            else:
                # {key, value}
                # {number, idx}
                seenNums[nums[i]] = i

#Hashmap solution: 23/23 test cases @ 7.7MB, 27ms


