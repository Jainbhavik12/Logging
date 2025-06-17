from collections import deque, defaultdict


logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

modifiedLogs = []

logsDict = defaultdict(list)
recent_logs = deque(maxlen=2)
freqlog = defaultdict(list)

def add_log(line: str) -> None:

    list1 = line.split()

    timeStamp = list1[0]
    timeStamp = timeStamp[1: len(timeStamp)-1]

    level = list1[1]


    userid = list1[2]
    userid = userid[:len(userid)-1]

    logsDict[userid] = level
    freqlog[level] = freqlog.get(level, 0)+1

    message = str(list1[3:])


    modifiedLogs.append({
            "TimeStamp" : timeStamp,
            "Level" : level,
            "UserId" : userid,
            "Message" : message
        })

def recent_log(line: str) -> None:
    for log in logs:
        recent_logs.append(log)

for log in logs:
    add_log(log)
    recent_log(log)


print(logsDict)
print(recent_logs)
print(freqlog)
print(modifiedLogs)









