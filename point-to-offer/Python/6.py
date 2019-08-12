# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        
        if len(rotateArray) == 1:
            return rotateArray[0]

        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]

        if len(rotateArray) == 2:
            return rotateArray[1]

        left = 0
        right = len(rotateArray) - 1
        while left < right:
            mid = (int)((left + right) / 2)
            
            if rotateArray[mid] < rotateArray[mid - 1]:
                break

            if rotateArray[mid] > rotateArray[0]:
                left = mid
            else:
                right = mid
        
        return rotateArray[mid] 

if __name__ == "__main__":
    so = Solution()
    array = [3, 4, 5, 1, 2]
    result = so.minNumberInRotateArray(array)
    print(result)