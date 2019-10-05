
# Must return an integer that denotes minimum possible value of unfairness
# k is the number of elements in the array
# arr is the array of integers

n = int(input())
k = int(input())

arr = sorted([int(input()) for _ in range(n)])
min_fairness = float('inf')

for i in range(k - 1, n):
    min_fairness = min(min_fairness, arr[i] - arr[i - k + 1])

print (min_fairness)
