from log_manager import LogRepository

def get_log_counts(logger: LogRepository, field: str):
    logs = logger.load_logs()

    log_counts = {}
    for log in logs:
        ip = log[field]

        if ip in log_counts:
            log_counts[ip] += 1
        else:
            log_counts[ip] = 1    
    return log_counts

def most_common_ip(logger: LogRepository):
    log_counts = get_log_counts(logger, "ip_address")

    most_common_ip = max(log_counts, key=log_counts.get)
    return most_common_ip


def most_targeted_user(logger: LogRepository):
    log_counts = get_log_counts(logger, "username")

    most_targeted_user = max(log_counts, key=log_counts.get)
    return most_targeted_user


def failed_login_counts(logger: LogRepository):
    log_counts = get_log_counts(logger, "event_type")

    return log_counts["failed_login"]


def successful_login_counts(logger: LogRepository):
    log_counts = get_log_counts(logger, "event_type")

    if log_counts:
        return log_counts["successful_login"]


def unique_ip_count(logger: LogRepository):
    log_counts = get_log_counts(logger, "ip_address")
    return len(log_counts)



if __name__ == "__main__":
    logger = LogRepository("logs.json")
    print(most_common_ip(logger))
    print(most_targeted_user(logger))
    print(failed_login_counts(logger))
    print(successful_login_counts(logger))
    print(unique_ip_count(logger))