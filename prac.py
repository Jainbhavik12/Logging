from collections import deque, defaultdict

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]


modified_logs = []
logs_dict = defaultdict(list)
recent_logs = deque(maxlen=2)
freq_log = defaultdict(int)


def add_log(line: str) -> None:
    parts = line.split()

    timestamp = parts[0][1:-1]
    level = parts[1]
    user_id = parts[2][:-1]
    message = ' '.join(parts[3:])


    logs_dict[user_id].append(level)


    freq_log[level] += 1


    modified_logs.append({
        "TimeStamp": timestamp,
        "Level": level,
        "UserId": user_id,
        "Message": message
    })


    recent_logs.append(line)


for log in logs:
    add_log(log)

# Output
print("Logs per User ID (logs_dict):\n", dict(logs_dict))
print("\nRecent Logs (last 2 entries):\n", list(recent_logs))
print("\nFrequency of Log Levels (freq_log):\n", dict(freq_log))
print("\nModified Logs:\n", modified_logs)
