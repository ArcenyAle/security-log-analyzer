from log_manager import LogRepository
from analytics import failed_login_counts, successful_login_counts
from filter import get_logs_by_ip

from collections import Counter

def create_report(logger: LogRepository, report_name: str):
    logs = logger.load_logs()
    suspicious_ips = logger.get_suspicious_ips()
    total_logs = len(logs)
    failed_logins = failed_login_counts(logger)
    successful_logins = successful_login_counts(logger)
    suspicious_logins = len(set(suspicious_ips))
    most_attacked_user = get_logs_by_ip(logger, Counter(suspicious_ips).most_common(1)[0][0])[0]["username"]

    with open(report_name, 'w') as f:
        f.write(f'{total_logs}\n{failed_logins}\n{successful_logins}\n{suspicious_logins}\n{most_attacked_user}')

if __name__ == "__main__":
    logger = LogRepository("logs.json")
    logger.add_suspicious_ip("192.168.1.10")
    create_report(logger, "test1.txt")
