# -*- coding:utf-8 -*-

# 题目描述：
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

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