'''
Maximum sum such that no two elements are adjacent
Given an array of positive and negative numbers, find the maximum 
sum of a subsequence with the constraint that no 2 
numbers in the sequence should be adjacent in the array. 
So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 
should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.
'''

def find_largest_sum(nums):
	if len(nums) == 0:
		return 0

	second_last, last, prev  = None, None, None
	max_sum = float('-inf')

	for i in range(len(nums)):
		curr = None

		if nums[i] > 0:
			l = float('-inf') if last is None else last
			sl = float('-inf') if second_last is None else second_last
			curr = nums[i] + max(l, sl, 0)
			max_sum = max(max_sum, curr)
			
		if prev is not None:
			second_last = last
			last = prev
		prev = curr

	if max_sum == float('-inf'): # all negs
		return max(nums)
	return max_sum

print(find_largest_sum([1,2, -10, 3,-10, -20, 1]))
print(find_largest_sum([3, 1, 1, 5, 1]))
print(find_largest_sum([1, 0, 3, 9, 2]))
print(find_largest_sum([2, 4, 6, 2, 5]))
print(find_largest_sum([9, -1, -11, 0, 10, -100]))
print(find_largest_sum([10, 300, -30, 20, -10]))
print(find_largest_sum([10, 3000, 2, 2, -40, 20, -7000]))
print(find_largest_sum([3000, 2, 2, -40, 4]))
