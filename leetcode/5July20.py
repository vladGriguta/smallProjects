class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # brute force solution: transform integers to binary arrays of the same length and substract one from the other
        # then add up the absolute values of the non-zero elements
        
        x_bin = [int(digit) for digit in list('{0:0b}'.format(x))]
        y_bin = [int(digit) for digit in list('{0:0b}'.format(y))]
        
        max_digits = max(len(x_bin),len(y_bin))
        
        while len(x_bin) < max_digits:
            x_bin.insert(0,0)
            
        while len(y_bin) < max_digits:
            y_bin.insert(0,0)
        
        hdistance = 0
        for i in range(max_digits):
            if(x_bin[i]!=y_bin[i]):
                
                hdistance += 1
        
        return hdistance