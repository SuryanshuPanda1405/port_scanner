import socket
import sys

def scan_port(ip, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)  # set timeout before connect
            return s.connect_ex((ip, port)) == 0  # True if open
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False  # safely handle common exceptions
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python terrible_port_scanner.py <hostname>")
        sys.exit(1)

    host = sys.argv[1]
    try:
        ip = socket.gethostbyname(host)
        print(f"Scanning {ip}...")

        for port in range(1, 1025):
            if scan_port(ip, port):
                print(f"Port {port} is open")

    except socket.gaierror:
        print("Error: Invalid hostname. Could not resolve IP.")
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
        sys.exit()
