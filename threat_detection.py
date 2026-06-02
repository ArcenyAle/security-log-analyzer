from log_manager import LogRepository
from analytics import get_log_counts
from filter import get_logs_by_user
from datetime import datetime, timedelta

def identify_attack(logger: LogRepository, user: str) -> bool:
    user_logs = get_logs_by_user(logger, user)
    failed_logs = [log for log in user_logs if log["event_type"] == "failed_login"]
    timestamps = sorted([log["timestamp"] for log in failed_logs], reverse=True)
    datetimes = [datetime.fromisoformat(timestamp) for timestamp in timestamps]

    if len(datetimes) < 5:
        return False
    
    for x in range(1, 5):
        if (datetimes[0] - datetimes[x]) >= timedelta(minutes=10):
            return False
        
    if user_logs:
        ip_address = user_logs[0]["ip_address"]
    
    logger.add_suspicious_ip(ip_address)
    return True


if __name__ == "__main__":
    logger = LogRepository("logs.json")
    print(identify_attack(logger, "bob"))
