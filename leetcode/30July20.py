class Solution:    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        if set(s) > set(''.join(word for word in wordDict)):
            return []
        
        solution = []
        def wordBreakRecursive(remainingString,wordsInBranch):
            
            if remainingString == '':
                solution.append(str(wordsInBranch[1:]))
                
            for word in wordDict:
                if(len(remainingString)>=len(word) and remainingString[:len(word)] == word):
                    wordBreakRecursive(str(remainingString[len(word):]),
                                       wordsInBranch+' '+word)
        
        wordBreakRecursive(s,'')
        
        return solution
        