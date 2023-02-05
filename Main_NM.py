import subprocess
import time

# List of IP addresses to be monitored
ips = []

def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False

# Add IP addresses to the list
while True:
    print("Enter IP address to monitor or type 'q' to quit:")
    ip = input()
    if ip == 'q':
        break
    ips.append(ip)

# Continuously monitor the IP addresses
while True:
    for ip in ips:
        response = ping_ip(ip)
        if response:
            print("{} is up".format(ip))
        else:
            print("{} is down".format(ip))
    time.sleep(5)
