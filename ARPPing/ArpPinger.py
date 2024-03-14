import argparse
import scapy.all as scapy

class ARPPing():
    def __init__(self):
        print("ARPPing başlatıldı...")

    def getUserInput(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ipaddress', type=str, help="IP adresnizi girmelisiniz...")
        args = parser.parse_args()

        ##print(args.ipaddress)

        if args.ipaddress != None:
            return args
        else:
            print("ip adresini -i şeklinde yazmalısın")

    def arpAccept(self, ip):

        arp_request_pack = scapy.ARP(pdst=ip)
        broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combinedPackages = broadcastPacket / arp_request_pack

        (answeredList, unansweredList) = scapy.srp(combinedPackages, timeout=1)
        answeredList.summary()

if __name__ =="__main__":
    arp_ping = ARPPing()
    kullaniciGirdisi=arp_ping.getUserInput()
    arp_ping.arpAccept(kullaniciGirdisi.ipaddress)




