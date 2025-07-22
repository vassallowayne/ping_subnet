# ping_subnet
A Python script to identify reachable hosts within a given subnet by pinging each IP address.



## 📡 Ping Subnet Scanner

This script allows you to scan a given IPv4 subnet and identify which hosts are currently reachable via ICMP ping.

### 🔍 What It Does

- Accepts a subnet in CIDR notation (e.g., `192.168.1.0/24`) as input.
- Iterates through each host in the subnet.
- Pings each IP address using the system's `ping` command.
- Prints whether each host is reachable or not.
- Outputs a final list of reachable IPs.

### 🛠 Requirements

- Python 3.x
- Works on Unix-like systems (uses `ping -c 1`). To run on Windows, change `-c` to `-n` in the script.

### 🚀 Usage

```bash
python3 ping_subnet.py 192.168.1.0/24

