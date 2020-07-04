class Solution:
    def prisonAfterNDays(self, cells, N):
        # Idea: look for recurrent patterns -> the same cell distribution should repeat
        # every k iterations - find k
        
        # turn cells to tuple to have easier access to elements
        cells = tuple(cells)
        # dict to store previous
        lookup = {}
        
        # iterate at most N times
        while N:
            # store current prison
            lookup[cells] = N
            # decrement N
            N -= 1
            # compute next distribution of cells
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0])
            # if next distribution of cells has been seen before
            if cells in lookup:
                
                #assert(lookup[cells] - N in (14))
                
                # at what N did the previous same cell distribution happen?                
                seasonality = lookup[cells] - N
                
                # operating the N=M*seasonality+K remaining days on the prison is equivalent to
                # not doing anything for M*seasonality and operating for the K days
                # therefore, update N to K:
                N %= lookup[cells] - N
                
                break
        
        # now that N is a number which is way smaller (1,seaasonality), apply the
        # operation for N days
        while N:
            N -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0])
        return list(cells)
        
    
    
    
        """
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

        """
	    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
	        import copy
	        b = [0 for i in range(8)]
	        for _ in range(N):
	            for i in range(1,7):
	                b[i] = int(cells[i-1] == cells[i+1])
	            cells = copy.deepcopy(b)
	        return b
	    """


                
        
        