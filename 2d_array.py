
# Setup array and and split all values
arr = [list(map(int, input().split())) for _ in range(6)]
sum = -float('inf')

# Create a for statement that will print the highest sum after calculating
for row in range(len(arr) - 2):
    for col in range(len(arr[row]) - 2):
        sum = max(arr[row][col]
                  + arr[row][col + 1]
                  + arr[row][col + 2]
                  + arr[row + 1][col + 1]
                  + arr[row + 2][col]
                  + arr[row + 2][col + 1]
                  + arr[row + 2][col + 2], sum)

print(sum)
