class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n # To store ugly numbers 

        # 1 is the first ugly number 
        ugly[0] = 1

        # i2, i3, i5 will indicate indices for 2,3,5 respectively 
        i2 = i3 =i5 = 0

        # set initial multiple value 
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        # start loop to find value from ugly[1] to ugly[n] 
        for l in range(1, n): 

            # choose the min value of all available multiples 
            ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 

            # increment the value of index accordingly 
            if ugly[l] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if ugly[l] == next_multiple_of_3: 
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if ugly[l] == next_multiple_of_5:  
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        # return ugly[n] value 
        return ugly[-1] 
        
        
        """
        # L1 - list of multiples of 3 and 5
        L1 = sorted([(3**i)*(5**j) for i in range(10) for j in range(10)])
        
        # L1 - list of multiples of 2 and 5
        L2 = sorted([(2**i)*(5**j) for i in range(10) for j in range(10)])
        
        # L1 - list of multiples of 2 and 3
        L3 = sorted([(2**i)*(3**j) for i in range(10) for j in range(10)])
        """
        
        
        
        """
        k = int(n**(1/3)) + 1
        
        fives = [5**i for i in range(1,int(k))]
        threes = [3**i for i in range(1,int(k))]
        twos = [2**i for i in range(1,int(k))]
        
        ones = np.ones(len(fives),len(threes),len(twos))
        
        fives_vector, threes_vector, twos_vector = np.meshgrid(ones,fives, threes,twos)
            
        print(threes_vector)
        
        multiplication = np.multiply(fives_vector,threes_vector).ravel()
        
        print(multiplication)
        """
        
        
        