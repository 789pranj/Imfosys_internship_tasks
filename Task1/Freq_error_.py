def analyse(logs):
    map = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    frequent_message = {}

    for log in logs:
        data = log.split()
        detail = data[2]
        message = " ".join(data[3:])

        map[detail] += 1

        if detail == "ERROR":
            if message in frequent_message:
                frequent_message[message] += 1
            else:
                frequent_message[message] = 1

    most_common = None
    if frequent_message:
        sorted_errors = sorted(
            frequent_message.items(),
            key=lambda x: x[1],
            reverse=True
        )
        most_common = sorted_errors[0][0]

    return {
        "INFO": map["INFO"],
        "WARNING": map["WARNING"],
        "ERROR": map["ERROR"],
        "most_common_error": most_common
    }

    
logs = [
    "2026-01-02 10:15:32 INFO Application started",
    "2026-01-02 10:15:35 INFO User logged in",
    "2026-01-02 10:16:01 WARNING Disk space running low",
    "2026-01-02 10:16:15 ERROR Database connection failed",
    "2026-01-02 10:16:20 ERROR Database connection failed",
    "2026-01-02 10:16:45 INFO Data processed successfully",
    "2026-01-02 10:17:05 WARNING High memory usage detected",
    "2026-01-02 10:17:20 ERROR Timeout while connecting to service",
    "2026-01-02 10:17:45 INFO User logged out",
    "2026-01-02 10:18:10 ERROR Database connection failed",
    "2026-01-02 10:18:30 INFO Application shutdown",
    "2026-01-02 10:19:00 ERROR Timeout while connecting to service"
]

data = analyse(logs=logs)

print(data)