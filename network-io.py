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

while True:
    os.system('clear')
    net_usage()
    time.sleep(1)