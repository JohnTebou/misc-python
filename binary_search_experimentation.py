arr1 = [2,3,4,6,9,12,89,11,8,6,4,1]
arr2 = [0, 1, 2, 3, 1.5, -4]

# find maximum
# find the last true if true means greater than the previous value
def findpeak(arr):
	l = 0
	r = len(arr) - 1
	ans = arr[0]

	while l <= r:
		m = l + (r - l) // 2
		if arr[m] > arr[m-1] if m > 0 else float("-inf"):
			ans = arr[m]
			l = m + 1
		else:
			r = m - 1
	return ans

print(findpeak(arr1))
print(findpeak(arr2))