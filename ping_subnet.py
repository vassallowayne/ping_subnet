import subprocess
import ipaddress
import argparse

def ping_ip(ip):
    """Ping an IP address and return True if it is reachable, False otherwise."""
    try:
        # Use `ping` command with `-c 1` for Unix-like systems or `-n 1` for Windows
        output = subprocess.check_output(['ping', '-c', '1', str(ip)], stderr=subprocess.STDOUT, universal_newlines=True)
        return "1 packets transmitted, 1 received" in output
    except subprocess.CalledProcessError:
        return False

def ping_subnet(subnet):
    """Ping all IP addresses in the given subnet and report which are reachable."""
    # Create an IP network object
    network = ipaddress.ip_network(subnet, strict=False)

    # Ping each IP in the network
    reachable_ips = []
    for ip in network.hosts():
        if ping_ip(ip):
            reachable_ips.append(ip)
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")

    return reachable_ips

def main():
    parser = argparse.ArgumentParser(description='Ping all IP addresses in a subnet.')
    parser.add_argument('subnet', type=str, help='The subnet to scan (e.g., 192.168.1.0/24)')
    args = parser.parse_args()

    # Ping the subnet
    reachable_ips = ping_subnet(args.subnet)
    print(f"\nReachable IPs: {reachable_ips}")

if __name__ == "__main__":
    main()
