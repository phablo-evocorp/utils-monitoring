import psutil, time, os


def net_usage():
    net_stats = psutil.net_io_counters()
    net_in_1 = net_stats.bytes_recv
    net_out_1 = net_stats.bytes_sent
    time.sleep(1)
    net_stats = psutil.net_io_counters()
    net_in_2 = net_stats.bytes_recv
    net_out_2 = net_stats.bytes_sent
   
    net_in = round((net_in_2 - net_in_1) * 8 / 1e6, 2)
    net_out = round((net_out_2 - net_out_1) * 8 / 1e6, 2)
   
    print(f"Up: {net_out} Mbps Down: {net_in}")
    return net_in, net_out

def net_errors():
    net_error = psutil.net_io_counters()
    print(f"Errors in receive: {net_error.errin}")
    print(f"Errors in send: {net_error.errout}")
    print(f"Packets droped in receive: {net_error.dropin}")
    print(f"Packets droped in send: {net_error.dropout} \n")

while True:
    os.system('clear')
    net_usage()
    net_errors()
    time.sleep(1)