import datetime
import re

pattern = pattern = re.compile(r"([A-Za-z])+([A-Za-z0-9]{2})", re.IGNORECASE)

def wrap_count_timings(count_timings, cur_packet):
    for _ in count_timings:
        #print(_.time_last_update)
        #print(cur_packet["time"])
        diff = (cur_packet["time"] - _.time_last_update).seconds
        #print(f"Difference: {diff} seconds")
        if diff < _.timing:
            _.total_count += 1
            if 'is_arp' in cur_packet:
                _.arp_count +=1
            if 'is_icmp' in cur_packet:
                _.icmp_count +=1
            if 'is_tcp' in cur_packet:
                _.tcp_count +=1
                #print(f"Period: {_.timing} seconds, total_number: {_.total_count}")
            if 'is_udp' in cur_packet:
                _.udp_count +=1
            if 'http_request' in cur_packet:
                _.http_request +=1
            if 'http_response' in cur_packet:
                _.http_response +=1
            if 'modbus_type' in cur_packet:
                if 'Request' in cur_packet["modbus_type"]:
                    f_code = (pattern.search(cur_packet["modbus_type"]).group(2))
                    f_code = int(f_code, 16)
                    exec('_.modbus_{:02}_request +=1'.format(f_code))
                else:
                    f_code = (pattern.search(cur_packet["modbus_type"]).group(2))
                    f_code = int(f_code, 16)
                    exec('_.modbus_{:02}_response +=1'.format(f_code))
        elif diff > _.timing:
            print(f"Let's send it: {_.timing} interval with {_.total_count} packets")
            temp_timing = _.timing
            _.send_to_server()
            _.__init__(datetime.datetime.now())
            _.timing = temp_timing
            print(f"Sended, now in counter {_.total_count} packets")
            
                
        