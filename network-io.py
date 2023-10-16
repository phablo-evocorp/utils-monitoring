import psutil, time, os

old_bytes_recv = 0
old_bytes_sent = 0

while True:
    os.system('clear')
    
    net_stats = psutil.net_io_counters()
    
    
    print("Network bytes in: ", net_stats.bytes_recv - old_bytes_recv)
    print("Network bytes out: ", net_stats.bytes_sent - old_bytes_sent)
    print("Network packets send: ", net_stats.packets_sent)
    print("Network packets receive: ", net_stats.packets_recv)
    print("Packets error in: ", net_stats.errin)
    print("Packets error out: ", net_stats.errout)
    print("Drop packets in: ", net_stats.dropin)
    print("Drop packets out: ", net_stats.dropout)
    time.sleep(1)
    
    old_bytes_recv = net_stats.bytes_recv
    old_bytes_sent = net_stats.bytes_sent