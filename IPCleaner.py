#!/usr/bin/env python3
import argparse
import sys
import re
from classes.IP import IP

# Global variables.
parser = argparse.ArgumentParser()
# parser.add_argument("input", help="Input file to extract IP addresses from.", metavar="<input-file-name>")
parser.add_argument("-o","--output", help="Output file", metavar="<output-file-name>")
parser.add_argument("-q", "--quite", help="Output IP addresses only", action="store_true")
parser.add_argument("-c", "--calc", help="Calculate network information for an IP")
parser.add_argument("-s", "--search", help="File to extract IP addresses from", metavar="<input-file-to-search>")
args = parser.parse_args()

def banner():
	# Prints the programs banner, usually the most important step.
	if not args.quite:
		print(
'''
  _____ _____   _____ _                            
 |_   _|  __ \ / ____| |                           
   | | | |__) | |    | | ___  __ _ _ __   ___ _ __ 
   | | |  ___/| |    | |/ _ \/ _` | '_ \ / _ \ '__|
  _| |_| |    | |____| |  __/ (_| | | | |  __/ |   
 |_____|_|     \_____|_|\___|\__,_|_| |_|\___|_|  
 v0.0.3
'''
)

def main():
	if args.search:
		input_file_name=args.search
		output_file_name = args.output
		host_list = get_hosts(input_file_name)

		if len(host_list) > 0:
			unique_hosts = unique(host_list)
			write_output(unique_hosts, output_file_name)
			cli_plus_print('The IPs have been cleansed...')
		else:	
			cli_negative_print("No IP addresses found.")

	elif args.calc:
		input_host = args.calc
		ip_obj = handle_mask_or_no_mask(input_host)
		if ip_obj:
			calc_print(ip_obj)
		else:
			cli_negative_print('Not a valid IP address...')

def calc_print(ip_obj):
	print('{:<19} {:<16} {:<34}'.format('IP Address:', ip_obj.ip_addr, ip_obj.ip_addr_binary))
	print('{:<19} {:<16} {:<34}'.format('Subnet Mask:', ip_obj.subnet_mask, ip_obj.subnet_mask_binary))
	print('{:<19} {:<16} {:<34}'.format('Network Address:', ip_obj.network_addr, ip_obj.network_addr_binary))
	print('{:<19} {:<16} {:<34}'.format('Broadcast Address:', ip_obj.broadcast_addr, ip_obj.broadcast_addr_binary))
	print('{:<19} {:<16}'.format('Num Hosts:', ip_obj.num_hosts_network))

def unique(host_list):
	unique_host_list = []
	unique_host_objects = []
	cli_plus_print("Removing duplicates...")

	for host in host_list:
		host_ip = host.ip_addr
		if host_ip not in unique_host_list:
			unique_host_list.append(host_ip)
			unique_host_objects.append(host)
		
	unique_host_objects.sort(key=lambda s: list(map(int, s.ip_addr.split('.'))))
	return unique_host_objects

def get_hosts(file_name):
	found_ips = []
	try:
		f=open(file_name, "r")
	except:
		cli_negative_print("Input file '{}' not found...".format(file_name))
		sys.exit()
	else:
		cli_plus_print("Reading input...")
		data = f.read()
		f.close()
		cli_plus_print("Searching for IP adresses...")
		host_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/?\d{0,2}", data)
		for host in host_list:
			ip_obj = handle_mask_or_no_mask(host)
			if ip_obj:
				found_ips.append(ip_obj)
				
	return found_ips

def write_output(unique_hosts, output_file_name):
	if args.output:
		try:
			unique_host_file = open(output_file_name, "w+")
		except:
			cli_negative_print('Unable to create file to write output...')
			sys.exit()
		else:
			cli_plus_print("Writing IPs to {}".format(output_file_name))
			for addr in unique_hosts:
				unique_host_file.write("\n{}{}".format(addr.network_addr, addr.cidr))
	else:
		for addr in unique_hosts:
			print('{}{}'.format(addr.ip_addr, addr.cidr))

def cli_plus_print(some_string):
	if not args.quite:
		print('[+] {}'.format(some_string))

def cli_negative_print(some_string):
	print('[-] {}'.format(some_string))

def validate_ip(ip):
	try:
		octet_list = ip.split('.')
	except:
		return False
	else:
		if len(octet_list) < 4:
			return False

		for octet in octet_list:
			try:
				decimal = int(octet)
				if decimal > 255 or decimal < 0:
					return False
			except:
				return False
	return True

def handle_mask_or_no_mask(host):
	if '/' in host:
		split_host = host.split('/')
		try:
			ip = split_host[0]
			mask = '/' + split_host[1]
		except:
			cli_negative_print('Host passed in incorrect format...')
		else:
			if validate_ip(ip):
				return IP(ip, mask)
				
	elif validate_ip(host):
		return IP(host)
	
	return False

if __name__ == '__main__':
	banner()
	main()
