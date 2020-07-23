def topKFrequent(nums, k):
    number_frequency = {}
    for i in nums:
        if i not in number_frequency:
            number_frequency[i] = 1
        else:
            number_frequency[i] += 1
    
    sorted_freq = {k: v for k, v in sorted(number_frequency.items(), key=lambda item: item[1], reverse=True)}
    
    return list(sorted_freq.keys())[:k]


print(topKFrequent([1,1,1,2,2,3],2))