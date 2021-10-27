n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
visited = [False] * (n+1)

def DFS(index, start, n, m):
    if index == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        DFS(index+1, i+1, n, m)

        s. pop()
        visited[i] = False

DFS(0, 0, n, m)