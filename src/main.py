import scapy.all as scapy
from tabulate import tabulate

def main():
	station, client = escanear_red("192.168.1.0/24", "eth0")

	imprimir_tabla("Estacion", station)
	imprimir_tabla("Clientes", client)

def escanear_red(ip, interface):
	arp = scapy.ARP(pdst=ip)
	ether = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")

	answer, _ = scapy.srp(ether/arp, timeout=1, iface=interface, verbose=False)

	station = [{"ip": arp.psrc, "mac": arp.hwsrc}]
	client = [{"ip": received.psrc, "mac": received.hwsrc} for _, received in answer]
	
	return station, client

def imprimir_tabla(name, elements):
	print(f"\n{name}:")
	print(tabulate(elements, headers="keys", showindex="always", tablefmt="fancy_grid"))

if __name__ == "__main__":
	main()
