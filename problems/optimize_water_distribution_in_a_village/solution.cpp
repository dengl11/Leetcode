class Solution {
    vector<int> uf;
    
public:
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
        uf.resize(n + 1, 0);
        for (auto &p : pipes) swap(p[0], p[2]);
        for (int i = 0; i < n; i ++) {
            uf[i + 1] = i + 1;
            pipes.push_back({wells[i], 0, i + 1});
        }
        sort(pipes.begin(), pipes.end());
        int res = 0;
        for(auto &p : pipes) {
            int ri = find(p[1]);
            int rj = find(p[2]);
            if (ri != rj) {
                n --;
                res += p[0];
                uf[ri] = rj;
            }
            if (n == 0) return res;
        }
        return res;
    }
    
    int find(int i) {
        if (uf[i] != i) {
            uf[i] = find(uf[i]);
        }
        return uf[i];
    }
};