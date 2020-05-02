class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        vector<int> presum(n+1);
        for (int i = 1; i <= n; i++) {
            presum[i] = presum[i-1] + cardPoints[i-1];
        }
        // for (auto x : presum) std::cout << x << std::endl;
        int total = presum[n];
        int min = total;
        for (int j = 0; j <= k; j ++) {
            min = std::min(min, presum[j + n - k] - presum[j]);
        }
        return total - min;
    }
};