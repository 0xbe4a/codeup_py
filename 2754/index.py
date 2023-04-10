n = int(input())
m = int(input())
nums = list(map(int, input().split()))

def dfs(idx, value):
    global cnt
    if idx == m:
        if value == n:
            cnt += 1
        return
    dfs(idx+1, value+nums[idx])
    dfs(idx+1, value-nums[idx])
print(cnt)
