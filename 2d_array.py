
arr = [list(map(int, input().split())) for _ in range(6)]
sum = -float('inf')

for row in range(len(A) - 2):
    for col in range(len(A[row]) - 2):
        sum = max(arr[row][col]
                  + arr[row][col + 1]
                  + arr[row][col + 2]
                  + arr[row + 1][col + 1]
                  + arr[row + 2][col]
                  + arr[row + 2][col + 1]
                  + arr[row + 2][col + 2], sum)

print(sum)
