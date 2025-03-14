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

# don't use ceiling/floor to calculate middle if not working
# with indices or necessarily integral values
def findsqrt(x):
	l = 0
	r = -(-51*x // 100) # ceiling of 1/2*x plus some small constant
	tolerance = 1e-15 # error
	while r - l >= tolerance:
		m = l + (r - l) / 2
		if m*m > x:
			r = m
		else:
			l = m
	return l + (r - l) / 2

print(findsqrt(2))