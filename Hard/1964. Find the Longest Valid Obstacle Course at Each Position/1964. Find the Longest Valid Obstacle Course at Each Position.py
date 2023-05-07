class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        ans = []

        for i in range(len(obstacles)):
            index = bisect.bisect_right(lis, obstacles[i])

            if index == len(lis):
                lis.append(obstacles[i])
            else:
                lis[index] = obstacles[i]

            ans.append(index+1)

        return ans