#network metrics exporter from prometheus client
from prometheus_client import start_http_server, Gauge
import psutil, time, os

gauge_error_in = Gauge('receive_errors_network', 'Errors in receive')
gauge_error_out = Gauge('send_errors_network', 'Errors in send')
gauge_drop_packets_in = Gauge('drop_packets_network_in', 'Packets droped in')
gauge_drop_packets_out = Gauge('drop_packets_network_out', 'Packets droped out')

net_stats = psutil.net_io_counters()


if __name__ == '__main__':
    start_http_server(8181)
    while True:
        gauge_error_in.set(net_stats.errin)
        gauge_error_out.set(net_stats.errout)
        gauge_drop_packets_in.set(net_stats.dropin)
        gauge_drop_packets_out.set(net_stats.dropout)
        time.sleep(1)