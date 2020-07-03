class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # 1. Starting with Day 1, the first and last cells will always be empty
        
        # first step not supported
        init_cells = [0 for i in range(8)]
        for i in range(1,7):
            init_cells[i] = int(cells[i-1] == cells[i+1])
        
        if N==1: return cells
        elif N==2:
            return init_cells
        else:
            import numpy as np
            m = np.array([[0,-1,0,0,0,0],
                          [-1,0,-1,0,0,0],
                          [0,-1,0,-1,0,0],
                          [0,0,-1,0,-1,0],
                          [0,0,0,-1,0,-1],
                          [0,0,0,0,-1,0]])
            a = np.array([1,1,1,1,1,1]).transpose()
            
            temp_array = np.array(init_cells[1:-1])
            
            for i in range(1,N):
                temp_array = np.absolute(a+np.matmul(m,temp_array))
            
            temp_array = list(temp_array)
            temp_array.insert(0,0)
            temp_array.append(0)
            
            return temp_array
        
        
        """
        # brute force
        new_cells = [0 for i in range(8)]
        
        def f(a,N):
            if N==1:
                for i in range(1,7):
                    new_cells[i] = a[i]
            
            else:
                b = [0 for i in range(8)]
                for i in range(1,7):
                    b[i] = int(a[i-1] == a[i+1])
                f(b,N-1)
        
        f(cells,N+1)
        
        return new_cells
        """
        
                
        
        