const int INF = 1e9 + 7;

class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        arr2.resize(unique(arr2.begin(), arr2.end()) - arr2.begin());
        int N = arr1.size(), M = arr2.size();
        vector<int> pre(M + 1, 1);
        pre[M] = 0;
        for (int i = 1; i < N; ++i) {
            vector<int> curr(M + 1, INF);
            // not replacing
            if (arr1[i] > arr1[i-1]) curr[M] = pre[M];
            
            for (int j = 0; j < M; ++j) {
                // replace with arr2[j]
                if (arr2[j] > arr1[i-1]) curr[j] = min(curr[j], pre[M] + 1);
                // previous position replaced with arr2[j]
                if (arr2[j] < arr1[i]) curr[M] = min(curr[M], pre[j]);
            }
            int mi = INF;
            for (int j = 0; j < M; ++j) {
                curr[j] = min(curr[j], mi + 1);
                mi = min(mi, pre[j]);
            }
            pre = curr;
        }
        int ans = *min_element(pre.begin(), pre.end());
        return ans != INF ? ans : -1;
        
            
    }
};