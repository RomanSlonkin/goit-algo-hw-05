import re 


def error_handler(func):
    def handler(*args):
        try:
            return func(*args)
        except IndexError:
            return('Log entry does not match the expected format')
        except FileNotFoundError:
            return('File not found or broken!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return handler

@error_handler
def parse_log_line(line: str) -> dict:
    log_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)'
    log = {}
    match = re.match(log_pattern, line)
    if match:
        log.update({'date': match.group(1), 'time': match.group(2), 'level': match.group(3), 'message': match.group(4) })
    else:
        print('Log entry does not match the expected format')
    return log
    
@error_handler
def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        logs = list()
        for line in lines:
            log = parse_log_line(line)
            if log:
                logs.append(log)
        return logs



def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    levels_count = {}
    for log in logs:
        level = log["level"]
        if level in levels_count:
            levels_count[level] += 1
        else:
            levels_count[level] = 1
    return levels_count

def display_log_counts(counts: dict):
    print(f"{'Level':<10} | {'Quantity':<15}")
    print('-'*27)
    for level, count in counts.items():
        print(f'{level:10} | {count:<15}')

