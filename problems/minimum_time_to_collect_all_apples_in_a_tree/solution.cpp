class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        int ans = 0;
        for (auto e : edges) {
            nbrs_[e[0]].push_back(e[1]);
            nbrs_[e[1]].push_back(e[0]);
        }
        std::set<int> visited;
        dfs(0, ans, visited, hasApple);
        return ans;
    }
    
    bool dfs(int curr, int& ans, std::set<int>& visited, vector<bool>& hasApple) {
        bool containApple = false;
        for (int j : nbrs_[curr]) {
            if (visited.find(j) != visited.end()) continue;
            visited.insert(j);
            containApple = dfs(j, ans, visited, hasApple) || containApple;
        }
        if (curr == 0) return false;
        if (containApple || hasApple[curr]) {
            ans += 2;
            return true;
        }
        return false;
    }
    
private:
    std::map<int, std::vector<int>> nbrs_;   
};