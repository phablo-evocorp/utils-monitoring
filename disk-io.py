import psutil, time, os

old_read_count = 0
old_write_count = 0
old_total_iops = 0
old_write_bytes = 0
old_read_bytes = 0

#disk_stats = psutil.disk_io_counters()

while True:
    os.system('clear')
    
    disk_stats = psutil.disk_io_counters()

    
    print("Operações de leitura por segundo: ", disk_stats.read_count - old_read_count)
    print("Operações de escrita por segundo: ", disk_stats.write_count - old_write_count)
    print("Total de operações por segundo: ", (disk_stats.read_count + disk_stats.write_count) - old_total_iops)
    print("Read megabytes per second: ", round((disk_stats.read_bytes - old_read_bytes) /1048576, 2))
    print("Write megabytes per second: ", round((disk_stats.write_bytes - old_write_bytes) /1048576, 2))
    
    old_read_count = disk_stats.read_count
    old_write_count = disk_stats.write_count
    old_write_bytes = disk_stats.write_bytes
    old_read_bytes = disk_stats.read_bytes
    old_total_iops = disk_stats.read_count + disk_stats.write_count
    
    time.sleep(1)
    