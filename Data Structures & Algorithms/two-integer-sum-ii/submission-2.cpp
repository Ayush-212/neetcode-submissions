class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::unordered_map<int,int>numMap;

        for(int i = 0; i<numbers.size();++i){
            int left = target-numbers[i];

            if(numMap.find(left)!= numMap.end()){
                return {numMap[left]+1,i+1};
            }
            numMap[numbers[i]] = i;
        }
        return {};
    }
};
