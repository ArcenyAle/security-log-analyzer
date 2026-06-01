from dataclasses import dataclass
from datetime import datetime

@dataclass
class LogEntry:
    id: int
    ip_address: str
    username: str
    event_type: str
    timestamp: str






if __name__ == "__main__":
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    test_log = LogEntry(1, "address", "name", "type", date)
    print(test_log.id)
    print(test_log.ip_address)
    print(test_log.username)
    print(test_log.event_type)
    print(test_log.timestamp)
    