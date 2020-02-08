#include <algorithm>

class UnionFind {
public:
    UnionFind(int n, vector<vector<int>>& connections) :n_(n) {
        roots.reserve(n);
        rank.reserve(n);
        fill(rank.begin(), rank.end(), 1);
        for (int i = 0; i < n; i ++) {
            roots[i] = i;
        }
        nC = n;
        for (vector<int> pair : connections) {
            union_two(pair[0], pair[1]);
        }
    }   
    
    int find(int i) {
        while (roots[i] != i) {
            i = roots[i];
        }
        return i;
    }
    
    void union_two(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i == root_j) return;
        nC -= 1;
        if (rank[root_i] < rank[root_j]) {
            int tmp = root_i;
            root_i = root_j;
            root_j = tmp;
        }
        roots[root_i] = root_j;
        if (rank[root_i] == rank[root_j])
            rank[root_i] += 1;
            
    }
    
    int nComponents() {
        return nC;
    }
    
    private:
    int n_;
    vector<int> roots;
    vector<int> rank;
    int nC;
    
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n-1) return -1;
        UnionFind uf = UnionFind(n, connections);
        return uf.nComponents() - 1;
        
    }
};