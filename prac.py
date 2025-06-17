from collections import defaultdict, deque

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]


def parse_log(func):
    def wrapper(log_str):
        parts = log_str.split(" ", 3)
        timestamp = parts[0].strip("[]")
        level = parts[1]
        user_id = parts[2].strip(":")
        message = parts[3]

        log_dict = {
            "TimeStamp": timestamp,
            "Level": level,
            "UserId": user_id,
            "Message": message
        }
        return func(log_dict)
    return wrapper


modified_logs = []
logs_dict = defaultdict(list)
recent_logs = deque(maxlen=2)
freq_log = defaultdict(int)

@parse_log
def add_log(log):
    user_id = log["UserId"]
    level = log["Level"]

    logs_dict[user_id].append(level)
    freq_log[level] += 1
    modified_logs.append(log)
    recent_logs.append(log)


for i in logs:
    add_log(i)


print("\n Logs per User ID:\n", dict(logs_dict))
print("\n Recent Logs:\n", list(recent_logs))
print("\n Frequency of Log Levels:\n", dict(freq_log))
print("\n Modified Logs:\n", modified_logs)
