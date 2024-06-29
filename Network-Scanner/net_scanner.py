
import optparse
import scapy.all as scapy


def scan_func(ip):
    arp_package = scapy.ARP(pdst=ip)

    broadcast_package = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    mix_package = arp_package/broadcast_package

    (answered_list, unanswered_list) = scapy.srp(mix_package, timeout=1)

    answered_list.summary()


def get_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-i", "--ipaddr", dest="input_ip")

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.input_ip:
        print("Enter IP Address")

    return user_input


user_ip = get_input()
scan_func(user_ip.input_ip)
