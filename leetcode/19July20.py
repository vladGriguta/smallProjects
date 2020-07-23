class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        L ← Empty list that will contain the sorted elements
        S ← Set of all nodes with no incoming edge

        while S is not empty do
            remove a node n from S
            add n to tail of L
            for each node m with an edge e from n to m do
                remove edge e from the graph
                if m has no other incoming edges then
                    insert m into S

        if graph has edges then
            return error   (graph has at least one cycle)
        else 
            return L   (a topologically sorted order)
            
        """
        
        courses = list(range(numCourses))
        
        orderedCourses = []
        
        # first append all courses that have no prerequisites
        courses_with_prerequisites = list(set([elem[0] for elem in prerequisites]))
        
        # append to orderedCourses the courses with no prerequisites. if none, return empty list
        courses_without_prerequisites = sorted(set(courses)-set(courses_with_prerequisites))
        
        print(courses_without_prerequisites)
        
        if not courses_without_prerequisites:
            return []
        
        
        while courses_without_prerequisites:
            orderedCourses.append(courses_without_prerequisites[-1])
            del courses_without_prerequisites[-1]
            
            print(orderedCourses)
            
            for i in range(len(prerequisites)):
                #print('gets here')
                print(prerequisites[i][1],' = ',orderedCourses[-1])
                
                if(prerequisites[i][1]==orderedCourses[-1]):
                    current_dependent_course = prerequisites[i][0]
                    
                    del prerequisites[i]
                    
                    print(current_dependent_course)
                    print([elem[0] for elem in prerequisites])
                    
                    # check if prerequisite[i][0] has any other prerequisites
                    if(current_dependent_course not in [elem[0] for elem in prerequisites]):
                        courses_without_prerequisites.insert(current_dependent_course,0)
            
            # if any unmet prerequisites left return empty:
            if prerequisites:
                return []
            else:
                return orderedCourses
                        
            
                        
                    
                    
                    
                
        
        
        
        
        