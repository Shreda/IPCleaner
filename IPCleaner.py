#!/usr/bin/env python3
'''
IPCleaner.py - A tool for searching files for IP addresses and performing subnetting on a given IP address and subnet mask.
'''
import argparse
import sys
import re
from classes.IP.IP import IP
from classes.IP.utils import validate_ip
from classes.IP.utils import unique
from classes.IP.utils import sort_ips
from classes.IP.utils import grep_ips
from classes.IP.utils import handle_mask_or_no_mask

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
		host_list = grep_ips(input_file_name)

		if len(host_list) > 0:
			unique_hosts = sort_ips(unique(host_list))
			write_output(unique_hosts, output_file_name)
			cli_plus_print('The IPs have been cleansed...')
		else:	
			cli_negative_print("No IP addresses found.")

	elif args.calc:
		input_host = args.calc
		ip_obj = handle_mask_or_no_mask(input_host)
		if ip_obj:
			print(ip_obj)
		else:
			cli_negative_print('Not a valid IP address...')

	else:
		parser.print_help()

# Takes a list of IP objects and an optional filename. If a filename is given,
# The network address and CIDR of the IP addresses is written to the file. 
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

# These functions handle the pretty terminal printing
def cli_plus_print(some_string):
	if not args.quite:
		print('[+] {}'.format(some_string))

def cli_negative_print(some_string):
	print('[-] {}'.format(some_string))

# True if the script is called from the command line
if __name__ == '__main__':
	banner()
	main()
