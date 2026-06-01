from datetime import datetime, timedelta

from log_manager import LogRepository
from data_structures import LogEntry



def get_failed_logins(logger: LogRepository):
    logs = logger.load_logs()

    return [log for log in logs if log["event_type"] == "failed_login"]



def get_successful_logins(logger: LogRepository):
    logs = logger.load_logs()

    return [log for log in logs if log["event_type"] == "successful_login"]



def get_logs_by_ip(logger: LogRepository, ip_address: str):
    logs = logger.load_logs()

    return [log for log in logs if log["ip_address"] == ip_address]



def get_logs_by_user(logger: LogRepository, username: str):
    logs = logger.load_logs()

    return [log for log in logs if log["username"] == username]



def get_logs_by_date(logger: LogRepository, date):
    logs = logger.load_logs()

    return [log for log in logs if log["timestamp"] == date]


if __name__ == "__main__":
    logger = LogRepository("logs.json")
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    date2 = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
    test_log = LogEntry(1, "address", "name", "failed_login", date)
    test_log1 = LogEntry(2, "address1", "name1", "successful_login", date2)
    logger.save_logs([test_log, test_log1])
    print(logger.load_logs())
    print("\nFAILED LOGINS BELOW\n")
    print(get_failed_logins(logger))
    print("\nSUCCESSFUL LOGINS BELOW\n")
    print(get_successful_logins(logger))
    print("\nADDRESS LOGINS BELOW\n")
    print(get_logs_by_ip(logger, "addressss"))
    print("\nNAME1 LOGINS BELOW\n")
    print(get_logs_by_user(logger, "name1"))
    print("\nDATE LOGINS BELOW\n")
    print(get_logs_by_date(logger, date))