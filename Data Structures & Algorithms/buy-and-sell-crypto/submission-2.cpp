class Solution {
public:
    int maxProfit(vector<int>& prices) {
     int profit = 0;
     int minP = INT_MAX;

     for(int i = 0;i<prices.size();i++){
        if(prices[i]<minP){
            minP = prices[i];
        } else if(prices[i]-minP>profit){
            profit = prices[i]-minP;
        }
     }
     return profit;
    }
};
