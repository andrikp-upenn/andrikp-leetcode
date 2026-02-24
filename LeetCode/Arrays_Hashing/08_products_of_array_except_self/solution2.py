class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        INPUT: Given an integer array nums,
        OUTPUT: Return an array output where output[i] = 
        product of all elem. of nums except nums[i]

        Constrains: Constraints:
        2 <= nums.length <= 1000
        -20 <= nums[i] <= 20

        example:
        nums = [1, 2, 4, 6]
        i = 0 --> 2*4*6 = 48
        i = 1 --> 1*4*6 = 24
        i = 2 --> 1*2*6 = 12
        """
        # Brute force O(n^2)

        result = []
        n = len(nums)
        for i in range(n):
            product = 1 # Reset for each i
            for j in range(n):
                if i == j:
                    continue
                product = product * nums[j]

            result.append(product)
        return result

# O(n^2) 19/19 test cases @ 29ms / 7.9MB - Suboptimal
                