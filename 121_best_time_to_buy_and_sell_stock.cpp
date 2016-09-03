class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret = 0;
        int min = 999999;
        int size = prices.size();
        for(int i = 0; i< size; ++i){
            if( min > prices[i] ) min = prices[i];
            else if ( prices[i] - min > ret ){
                ret = prices[i] - min;
            }
        }
        return ret;
    }
};
