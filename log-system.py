from datetime import datetime

def log_factory():
    def log(msg, timestamp=True, log_level=None, events=None):
        log_entry = {'msg': msg}
        
        if timestamp:
            log_entry['timestamp'] = datetime.now()
        
        if log_level:
            log_entry['log_level'] = log_level
        
        if events:
            log_entry['events'] = events
        
        return log_entry

    return log

def log_processor_factory():
    def filter_logs(logs, no_timestamp=False, timestamp_range=None, short_msg=True):
        filtered_logs = logs
        
        if no_timestamp:
            filtered_logs = [log for log in filtered_logs if 'timestamp' not in log]
        
        if timestamp_range:
            start, end = timestamp_range
            filtered_logs = [log for log in filtered_logs if 'timestamp' in log and start <= log['timestamp'] <= end]
        
        if short_msg:
            filtered_logs = [log for log in filtered_logs if 'msg' in log and len(log['msg']) < 10]
        
        return filtered_logs

    return filter_logs

# Example Usage:

# Create log and log processor functions
log = log_factory()
log_processor = log_processor_factory()

# Create some logs
logs = [
    log("This is a simple log message."),
    log("Log with timestamp and info level.", log_level="info"),
    log("Warning log with events.", log_level="warn", events=["event1", "event2"]),
    log("Log with timestamp and longer message.", timestamp=True),
]

print("All Logs:")
for log_entry in logs:
    print(log_entry)

filtered_logs = log_processor(logs, no_timestamp=True)
print("\nFiltered Logs (No Timestamp):")
for log_entry in filtered_logs:
    print(log_entry)

filtered_logs = log_processor(logs, timestamp_range=(datetime.now(), datetime.now()))
print("\nFiltered Logs (Timestamp Range):")
for log_entry in filtered_logs:
    print(log_entry)

filtered_logs = log_processor(logs, short_msg=True)
print("\nFiltered Logs (Short Msg):")
for log_entry in filtered_logs:
    print(log_entry)
