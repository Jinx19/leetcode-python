from collections import deque
queue = deque([1, 2, 3])
queue.append(43)
print(queue.popleft())
