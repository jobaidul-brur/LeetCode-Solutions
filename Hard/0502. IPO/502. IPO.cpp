class MaxSegTree {
    struct Node{
        Node *left, *right;
        int val; int idx;
        Node() {
            left = right = nullptr; val = -1, idx = -1;
        }
    };
    int N; Node *root;
public:
    MaxSegTree() {}
    MaxSegTree(int n) {
        N = 1LL<<(ilogb(n)); if (N < n) N += N;
        root = new Node();
    }
    void set(int k, int val) {
        set(root, 0, N-1, k, k, val);
    }
    pair<int, int> maxq(int l, int r) {
        return maxq(root, 0, N-1, l, r);
    }
private:
    void set(Node *node, int nl, int nr, int ql, int qr, int val) {
        if (ql <= nl and nr <= qr) {
            node->val = val;
            node->idx = ql;
            return;
        }
        int mid = (nl + nr) / 2;
        if (ql <= mid) {
            if (node->left == nullptr) node->left = new Node();
            set(node->left, nl, mid, ql, qr, val);
        }
        if (mid < qr) {
            if (node->right == nullptr) node->right = new Node();
            set(node->right, mid+1, nr, ql, qr, val);
        }
        pair<int, int> left = {-1, -1}, right = {-1, -1};
        if (node->left != nullptr) left = {node->left->val, node->left->idx};
        if (node->right != nullptr) right = {node->right->val, node->right->idx};
        if (left.first > right.first) {
            node->val = left.first;
            node->idx = left.second;
        } else {
            node->val = right.first;
            node->idx = right.second;
        }
    }
    pair<int, int> maxq(Node *node, int nl, int nr, int ql, int qr) {
        if (node == nullptr) return {-1, -1};
        if (ql <= nl and nr <= qr) return {node->val, node->idx};
        int mid = (nl + nr) / 2;
        pair<int, int> left, right;
        if (ql <= mid) left = maxq(node->left, nl, mid, ql, qr);
        if (mid < qr) right = maxq(node->right, mid+1, nr, ql, qr);
        if (left.first > right.first) return left;
        else return right;
    }
};
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        map<int, vector<int>> mp;
        for (int i = 0; i < profits.size(); ++i) {
            mp[capital[i]].push_back(profits[i]);
        }
        MaxSegTree tree(1e9+10);
        for (auto &it : mp) {
            sort(it.second.begin(), it.second.end());
            tree.set(it.first, it.second.back()); it.second.pop_back();
        }
        int captl, proft;
        for (int i = 0; i < k; ++i) {
            tie(proft, captl) = tree.maxq(0, w);
            if (proft == -1) {
                break;
            }
            w += proft;
            if (mp[captl].size() > 0) {
                tree.set(captl, mp[captl].back()); mp[captl].pop_back();
            } else {
                tree.set(captl, -1);
            }
        }
        return w;
    }
};
