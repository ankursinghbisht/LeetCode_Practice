import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        # Create a Counter to count the frequency of each number
        frequency_counter = Counter(nums)

        # Use a min heap to keep track of the top k frequent elements
        min_heap = []

        for num, freq in frequency_counter.items():
            # Push a tuple with frequency and number
            heapq.heappush(min_heap, (freq, num))

            # If the heap size exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Retrieve the top k frequent elements from the heap
        top_k_elements = [num for freq, num in min_heap]

        # Reverse the list to get the elements in non-decreasing order of frequency
        return top_k_elements[::-1]


