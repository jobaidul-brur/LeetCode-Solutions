class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (flowerbed.length == 1) {
            if (flowerbed[0] == 0) n--;
        }
        else {
            if (flowerbed[0] == 0 && flowerbed[1] == 0) {
                flowerbed[0] = 1;
                n--;
            }
            for (int i = 1; i < flowerbed.length; i++) {
                if (flowerbed[i] == 0 && flowerbed[i-1] == 0 &&(i+1 >= flowerbed.length || flowerbed[i+1] == 0)) {
                    flowerbed[i] = 1;
                    n--;
                }
            }
        }
        //System.out.println(Arrays.toString(flowerbed));
        return n <= 0;
    }
}