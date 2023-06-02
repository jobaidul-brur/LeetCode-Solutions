/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function(bombs) {
    let ans = 0;
    for (let start = 0; start < bombs.length; start++) {
        let count = 1;
        let visited = new Set();
        visited.add(start);
        let queue = [start];
        while (queue.length > 0) {
            let curr = queue.shift();
            for (let next = 0; next < bombs.length; next++) {
                if (visited.has(next)) continue;
                let [x1, y1, r1] = bombs[curr];
                let [x2, y2, r2] = bombs[next];
                if ((x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1) ** 2) {
                    visited.add(next);
                    queue.push(next);
                    count++;
                }
            }
        }
        ans = Math.max(ans, count);
    }
    return ans;
};
