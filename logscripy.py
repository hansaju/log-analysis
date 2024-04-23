import time
import signal
import sys

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    print('\nMonitoring stopped.')
    sys.exit(0)

# Function to monitor log file
def monitor_log(log_file, keywords):
    print("Monitoring log file:", log_file)
    try:
        with open(log_file, 'r') as file:
            # Move file pointer to the end
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                for keyword in keywords:
                    if keyword in line:
                        print(line.strip())
                        # Additional analysis can be performed here
    except FileNotFoundError:
        print("Error: Log file not found.")
        sys.exit(1)

# Main function
def main():
    if len(sys.argv) < 3:
        print("Usage: python log_monitor.py <log_file> <keyword1> [<keyword2> ...]")
        sys.exit(1)

    log_file = sys.argv[1]
    keywords = sys.argv[2:]

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Monitor log file
    monitor_log(log_file, keywords)

if __name__ == "__main__":
    main()
