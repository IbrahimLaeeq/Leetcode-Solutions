class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.preMap = collections.defaultdict(list)
        # this dictoinary maps to a list
        for crs, pre in prerequisites:
            self.preMap[crs].append(pre)
        
        # now create 3 sets for topolgical sort
        white = set((self.preMap.keys())) # eles that are left
        grey = set()  # children of currently visited ele
        black = set() # ele which has been fully processed

        while white:
            crs = white.pop()
            
            if not self.dfs(crs, grey , black):
                return False
        
        return True

    def dfs(self,course, grey, black):
        grey.add(course)
        # adding course to grey after popping from white

        for prereq in self.preMap[course]:
            if prereq in black:
                continue
            
            if prereq in grey:
                return False
            
            if not self.dfs(prereq, grey , black):
                # calling dfs again
                return False
        
        grey.remove(course)
        black.add(course)

        return True