#FIFO -> first in first out

from collections import deque 


row = deque([1, 2])
row.append(3)
row.append(4)
row.append(5)

print(row)

row.popleft()
print(row)

if not row: # [], '', 0 -> False
    print('row empty')