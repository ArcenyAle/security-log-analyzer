from log_manager import LogRepository
from filter import get_failed_logins

def yield_failed_logins(logger: LogRepository):
    failed_logs = get_failed_logins(logger)
    return (log for log in failed_logs)

if __name__ == "__main__":
    logger = LogRepository("logs.json")
    failed = yield_failed_logins(logger)
    print(next(failed))
    print(next(failed))
    print(next(failed))