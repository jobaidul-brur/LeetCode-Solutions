class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        for s in salary:
            sum += s
        sum -= salary[0]+salary[-1]
        print(sum)
        return sum/(len(salary)-2)
        
