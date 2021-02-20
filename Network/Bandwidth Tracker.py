import time
import psutil

usage = []

def main():
    old_value = 0    

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_gbit(value):
    value /= 1024
    usage.append(value)
    return value

def send_stat(value):
    print("%0.3f KB" % convert_to_gbit(value))
    print(usage)

main()