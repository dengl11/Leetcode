class Solution {
private:
    bool containsInterval(const vector<int>& prefix, int T) {
        // Whether there exists at least T day interval.
        int minsofar = prefix[0];
        for (int i = 0; i < prefix.size(); ++i) {
            minsofar = min(minsofar, prefix[i]);
            if (i + T < prefix.size() && prefix[i + T] > minsofar) return true;
        }
        return false;
    }
public:
    int longestWPI(vector<int>& hours) {
        int lo = 0, hi = hours.size();
        vector<int> prefix;
        prefix.push_back(0);
        for (int h : hours) {
            if (h > 8) prefix.push_back(prefix.back() + 1);
            else prefix.push_back(prefix.back() - 1);
        }
        while (lo < hi) {
            int mi = hi - (hi - lo) / 2;
            if (containsInterval(prefix, mi)) lo = mi;
            else hi = mi - 1;
        }
        return lo;
    }
};