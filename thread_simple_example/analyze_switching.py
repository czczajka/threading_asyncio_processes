import pandas as pd

data = pd.read_csv('result', encoding= 'unicode_escape')

counter = 0
prevThread = -1
for i, row in data.iterrows():
    if (row.values[0] == "Thread number: 0"):
        if (prevThread != 0):
            print("Thread: " + str(prevThread) + ",Counter: " + str(counter))
            prevThread = 0
            counter = 1
        else:
            counter = counter + 1

    if (row.values[0] == "Thread number: 1"):
        if (prevThread != 1):
            print("Thread: " + str(prevThread) + ",Counter: " + str(counter))
            prevThread = 1
            counter = 1
        else:
            counter = counter + 1

    if (row.values[0] == "Thread number: 2"):
        if (prevThread != 2):
            print("Thread: " + str(prevThread) + ",Counter: " + str(counter))
            prevThread = 2
            counter = 1
        else:
            counter = counter + 1
print("Thread: " + str(prevThread) + ",Counter: " + str(counter))
