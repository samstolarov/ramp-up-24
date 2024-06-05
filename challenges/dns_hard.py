import socket
def get_domain(ip_address):
	dest = socket.gethostbyaddr(ip_address)[0]
	return str(dest)
	