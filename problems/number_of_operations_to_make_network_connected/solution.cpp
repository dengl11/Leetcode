#include <algorithm>

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n-1) return -1;
        vector<vector<int>> nbrs(n);
        vector<int> seen(n, 0);
        for (const vector<int>& edge : connections) {
            nbrs[edge[0]].push_back(edge[1]);
            nbrs[edge[1]].push_back(edge[0]);
        }
        std::fill(seen.begin(), seen.end(), 0);
        std::function<int(int)> dfs;
        dfs =  [&](int i) -> int {
        if (seen[i]) return 0;
        seen[i] = 1;
        for (int j : nbrs[i]) dfs(j);
        return 1;
    };
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            ans += dfs(i);
        }
        return ans - 1;
    }

    
};