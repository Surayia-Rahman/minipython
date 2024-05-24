import requests
from scapy.all import ARP, Ether, srp

def get_vendor(mac_address):
    """
    Retrieves the vendor information for a given MAC address.

    Args:
        mac_address (str): The MAC address to lookup.

    Returns:
        str: The vendor name if found, otherwise "Unknown".
    """
    try:
        response = requests.get(f"https://api.macvendors.com/{mac_address}")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error occurred during MAC address lookup: {e}")
        return "Unknown"

def scan_network(target_ip_range="192.168.100.1/24", timeout=2):
    """
    Scans the specified IP range for devices using ARP requests.

    Args:
        target_ip_range (str, optional): The IP range to scan in CIDR notation. Defaults to "192.168.100.1/24" (based on your Wi-Fi configuration).
        timeout (int, optional): The timeout value in seconds for waiting for ARP responses. Defaults to 2.

    Returns:
        list: A list of dictionaries containing IP, MAC addresses, and vendor information of discovered devices.
    """

    # Create ARP request packet
    arp_request = ARP(pdst=target_ip_range)
    ether_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / arp_request

    # Send ARP requests and capture responses
    try:
        results, unanswered = srp(ether_packet, timeout=timeout, verbose=0)
    except Exception as e:
        print(f"Error occurred during ARP scan: {e}")
        return []

    # Extract IP, MAC addresses, and vendor information from responses
    clients = []
    for sent, received in results:
        mac_address = received.hwsrc
        vendor = get_vendor(mac_address)
        clients.append({'ip': received.psrc, 'mac': mac_address, 'vendor': vendor})

    return clients

# Example usage with adjusted target IP range based on your Wi-Fi configuration
discovered_devices = scan_network()

if discovered_devices:
    print("Available devices in the network:")
    print("IP" + " "*18 + "MAC" + " "*18 + "Vendor")
    for client in discovered_devices:
        print("{:16}    {}    {}".format(client['ip'], client['mac'], client['vendor']))
else:
    print("No devices found on the network.")
