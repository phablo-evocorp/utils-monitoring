import psutil, time, os

#disk_stats = psutil.disk_io_counters()

while True:
    os.system('clear')
    
    disk_stats = psutil.disk_io_counters()

    
    print("Operações de leitura: ", disk_stats.read_count)
    print("Operações de escrita: ", disk_stats.write_count)
    print("Total de operações por segundo: ", disk_stats.read_count + disk_stats.write_count)
    print("Read megabytes: ", disk_stats.read_bytes/1048576)
    print("Write megabytes: ", disk_stats.write_bytes/1048576, '\n')
    time.sleep(1)
    