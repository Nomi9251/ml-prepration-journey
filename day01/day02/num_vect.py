import numpy as np

#  mini house price predictor

def predict_price(feature, weight, bias):
    return np.dot(feature, weight) + bias

feature = np.array([1200, 3, 2])
weight = np.array([50, 20000, 9])
bias = 10000

price = predict_price(feature, weight,bias)
print(price)



class Solution(object):
    def maxSubArray(self, nums):
      pos = 0
      for i in range(len(nums)):
          if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

      return nums
s1 = Solution()
res = s1.maxSubArray([1,0, 2, 4, 0, 6,0 ,9])

print(res)