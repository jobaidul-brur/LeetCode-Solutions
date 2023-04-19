class Solution {
    int eat(int[] piles, int k) {
        int cnt = 0;
        for (int pile : piles) {
            cnt += (pile+k-1)/k;
        }
        return cnt;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 1_000_000_001, mid;
        while (lo < hi) {
            mid = lo+(hi-lo)/2;
            if (eat(piles, mid) <= h) hi = mid;
            else lo = mid+1;
        }
        return lo;
    }
}