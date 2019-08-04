#include <vector>

class Solution {
public:
    bool Find(int target, vector<vector<int> > array) 
    {
        int row = array.size();
        int col = array.front().size();

        int i = 0;
        int j = col - 1;
        while (i < row && j >= 0)
        {
            if (array[i][j] < target)
            {
                i++;
            }
            else if (array[i][j] > target)
            {
                j--;
            }
            else 
            {
                return true;
            }
        }

        return false;
    }
};