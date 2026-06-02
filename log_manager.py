import json
from datetime import datetime
from dataclasses import asdict

from data_structures import LogEntry

def datetime_to_str(time: datetime):
    return time.strftime("%Y-%m-%dT%H:%M:%S")

class LogRepository:
    def __init__(self, log_file):
        self.log_file = log_file
        self.suspicious_ips = []

    def add_suspicious_ip(self, ip: str):
        self.suspicious_ips.append(ip)

    def get_suspicious_ips(self) -> list[str]:
        return self.suspicious_ips
    
    def load_logs(self) -> list[LogEntry]:
        with open(self.log_file, 'r') as f:
            logs = json.load(f)

        return logs
    
    def save_logs(self, logs: list[LogEntry]):
        logs = [asdict(log) for log in logs]
        #my_logs = json.loads(logs)
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=4)

        return True
    
    def add_log(self, log_id: int, ip_address: str, username: str, event_type: str, timestamp: str | datetime):
        if type(timestamp) == datetime:
            timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%S")

        log = asdict(LogEntry(log_id, ip_address, event_type, username, timestamp))
        log_entries = self.load_logs()
        log_entries.append(log)

        with open(self.log_file, 'w') as f:
            json.dump(log_entries, f, indent=4)
        
        return True
    
    def delete_log(self, log_id: int):
        logs = self.load_logs()
        cleared_logs = [log for log in logs if log["id"] != log_id]

        with open(self.log_file, 'w') as f:
            json.dump(cleared_logs, f, indent=4)

        return True
    
    def get_logs_by_id(self, log_id: int):
        logs = self.load_logs()
        log = [l for l in logs if l["id"] == log_id]
        return log[0]

    def update_log(self, log_id: int, username: str | None = None, timestamp: str | datetime | None = None):
        if type(timestamp) == datetime:
            timestamp = datetime_to_str(timestamp)

        log_to_update = self.get_logs_by_id(log_id)
        if not log_to_update:
            return False

        self.delete_log(log_to_update["id"])

        if username:
            log_to_update["username"] = username

        if timestamp:
            log_to_update["timestamp"] = timestamp

        log = list(log_to_update.values())
        self.add_log(log[0], log[1], log[2], log[3], log[4])
        return True

        


        

if __name__ == "__main__":
    logger = LogRepository("logs.json")
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    test_log = LogEntry(1, "address", "name", "type", date)
    test_log1 = LogEntry(2, "address1", "name1", "type1", date)
    logger.save_logs([test_log, test_log1])
    print(logger.load_logs())
    logger.add_log(3, "ip3", "tuty", "testing", date)
    print(logger.load_logs())
    logger.delete_log(1)
    print("\n\n\n\n\n")
    print(logger.get_logs_by_id(3))
    logger.update_log(3, "YayItWorks3")
    logger.update_log(2, "YayItWorks2", date)