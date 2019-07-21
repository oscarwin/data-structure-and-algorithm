class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> vecRet;
        std::map<int, int> kv;
        for (size_t i = 0; i != nums.size(); ++i)
        {
            kv[nums[i]] = i;
            if (kv.find(target - nums[i]) != kv.end())
            {
                vecRet.push_back(kv[nums[i]]);
                vecRet.push_back(i);
                break;
            }
        }
        return vecRet;
    }
};