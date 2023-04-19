class BrowserHistory {
    vector<string> history;
    int pos, size;
public:
    BrowserHistory(string homepage) {
        history = vector<string>(10000);
        pos = 0;
        size = 0;
        history[size++] = homepage;
    }

    void visit(string url) {
        size = pos + 1;
        history[size++] = url;
        pos++;
    }

    string back(int steps) {
        pos = max(0, pos-steps);
        return history[pos];
    }

    string forward(int steps) {
        pos = min(size-1, pos+steps);
        return history[pos];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */