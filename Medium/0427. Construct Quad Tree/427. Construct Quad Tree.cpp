/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
    Node *solve(int r, int c, int len, vector<vector<int>>& grid) {
        bool zero = false, one = false;
        for (int i = r; i < r+len; i++) {
            for (int j = c; j < c+len; j++) {
                if (grid[i][j] == 1) one = 1;
                else zero = 1;
            }
        }
        if (zero == 0 or one == 0) {
            return new Node(grid[r][c], 1);
        }
        return new Node(0, 0, solve(r, c, len/2, grid), solve(r, c+len/2, len/2, grid),
            solve(r+len/2, c, len/2, grid), solve(r+len/2, c+len/2, len/2, grid));
    }
public:
    Node* construct(vector<vector<int>>& grid) {
        return solve(0, 0, grid.size(), grid);
    }
};
