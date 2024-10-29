from functions import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts
import sys


def main():
    if len(sys.argv) < 2:
        print("Please give me path to file")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        if any(log['level'] == level for log in logs):  # Перевірка наявності рівня
            filtered_logs = filter_logs_by_level(logs, level)
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
        else:
            print(f"No logs found for level: {level}")
        


if __name__ == '__main__':
    main()




