class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:set() for i in range(numCourses)}
        taken = set()
        for cur,pre in prerequisites:
            prereqs[cur].add(pre)
        
        def dfs(course):
            if course in taken:
                print(course, 'in taken', course, taken)
                return False
            numofprereqs = len(prereqs[course])
            if numofprereqs == 0:
                return True
            taken.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False  
            taken.remove(course)
            prereqs[course] = []
            return True
                

        for c in prereqs:
            if not dfs(c):
                print('its false')
                return False
            taken = set()
        return True
        
        