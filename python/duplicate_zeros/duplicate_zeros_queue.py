from collections import deque
ra = [0, 1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10]
q = deque()

for k in range(len(ra)):
    q.append(ra[k])
    if ra[k] == 0:
        q.append(ra[k])
    ra[k] = q.popleft()

print(ra)
