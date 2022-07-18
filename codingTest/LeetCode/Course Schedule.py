# 토폴로지 소트 문제
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canTake = [0]*(numCourses)
        precourses = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            canTake[a] += 1
            precourses[b].append(a)
        q = deque()
        for i, num in enumerate(canTake):
            if num == 0:
                q.append(i)
        while q:
            index = q.popleft()
            for pre in precourses[index]:
                canTake[pre] -= 1
                if canTake[pre] == 0:
                    q.append(pre)
        if sum(canTake) == 0:
            return True
        else:
            return False
            
