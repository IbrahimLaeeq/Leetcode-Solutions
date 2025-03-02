class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #hash table
        preMap = {i : [] for i in range(numCourses)}
        #populate the table
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
        visitSet = set()
        # declare set to find out if ele has already been visited before
        def dfs(crs):
            #base conditions
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True 
            # this means that we have taken all the pre requisites for 
            #this course so now we can take this course 

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            # now run dfs for the pre requisites of the current course too
            visitSet.remove(crs)#as we have processed all its pre requisites
            preMap[crs] = []
            # set the pre req for this course to an empty list indicating that 
            # we can take this course
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True