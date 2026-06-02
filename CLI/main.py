import sys
from pathlib import Path

# Allow imports from the project root when this file is run as a script.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from log_manager import LogRepository
from filter import *
from create_report import create_report
from threat_detection import identify_attack


def print_menu():
    print("1. Add a new log")
    print("2. Delete a log")
    print("3. Search logs")
    print("4. Create report")
    print("5. Detect threats")
    print("6. Exit")


def print_search_log_options():
    print("1. Search by IP address")
    print("2. Search by username")
    print("3. Search by date (Developer use only)")


def add_log(logger: LogRepository):
    id = input("Enter the log id: ")
    ip_address = input("Enter the IP address: ")
    username = input("Enter the username: ")
    event_type = input("Enter the event type: ")
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    logger.add_log(int(id), ip_address, username, event_type, timestamp)
    identify_attack(logger, username)
    print("Log added successfully")

def search_log(logger: LogRepository):
    print_search_log_options()
    choice = input("Enter a number for your choice: ")
    if choice == "1":
        print(get_logs_by_ip(logger, input("Enter the IP address: ")))
    elif choice == "2":
        print(get_logs_by_user(logger, input("Enter the username: ")))
    elif choice == "3":
        print(get_logs_by_date(logger, input("Enter the date in iso: ")))
    else:
        print("Invalid choice")




def cli():
    logger = LogRepository("logs.json")
    logger.clear_logs()
    while True:
        print_menu()
        choice = input("Enter a number for your choice: ")
        if choice == "6":
            logger.clear_logs()
            break
        elif choice == "1":
            add_log(logger)
        elif choice == "2":
            log_id = input("Enter the log id: ")
            logger.delete_log(int(log_id))
        elif choice == "3":
            search_log(logger)
        elif choice == "4":
            create_report(logger, input("Enter the report name: "))
        elif choice == "5":
            threats = logger.get_suspicious_ips()
            print(f'There are {len(threats)} threats')
        else:
            print("Invalid choice")
        
            

def main():
    cli()


if __name__ == "__main__":
    main()