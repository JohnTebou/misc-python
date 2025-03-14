import time
start_time = time.time()

def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# def fib2(n, memo):
# 	memo[0] = memo[1] = 1
# 	if memo[n-1]:
# 		return memo[n-1]
# 	else:
# 		memo[n-1] = fib2(n-1, memo) + fib2(n-2, memo)
# 		return fib2(n-1, memo) + fib2(n-2, memo)
	
def fib2(n, memo):
	if memo[n-1]:
		return memo[n-1]
	if n <= 2:
		return 1
	else:
		result = fib2(n-1, memo) + fib2(n-2, memo)
	memo[n-1] = result
	return result

def fib3(n):
	if n <= 2:
		return 1
	bottom_up = [1,1] + [None] * (n-2)
	for i in range(2, n):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	return bottom_up[-1]

# print(fib2(1000, [None]*1000))
print(fib3(1000))
print("--- %s seconds ---" % (time.time() - start_time))