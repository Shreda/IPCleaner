import sys
import re
from classes.IP.IP import IP

def validate_ip(ip):
    # Takes a string and does some magic to make sure it is a valid IP
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


def sort_ips(IP_obj_list):
    '''
    Takes a list of IP objects as input sorts them and returns them.
    '''
    IP_obj_list.sort(key=lambda s: list(map(int, s.ip_addr.split('.'))))
    return IP_obj_list


def unique(IP_obj_list):
    '''
    Takes a list of IP objects as input and removes duplicate entries based on
    the stored ip_addr string.
    '''
    unique_host_list = []
    unique_host_objects = []

    for host in IP_obj_list:
        host_ip = host.ip_addr
        if host_ip not in unique_host_list:
            unique_host_list.append(host_ip)
            unique_host_objects.append(host)
        
    return unique_host_objects


def grep_ips(file_name):
    '''
    Takes a file as input and uses a regular expression to find regular IP addresses with or without a CIDR.
    From this, it creates IP objects and returns them in a list.
    '''
    found_ips = []
    try:
        f=open(file_name, "r")
    except:
        # cli_negative_print("Input file '{}' not found...".format(file_name))
        sys.exit()
    else:
        # cli_plus_print("Reading input...")
        data = f.read()
        f.close()
        # cli_plus_print("Searching for IP adresses...")
        host_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/?\d{0,2}", data)
        for host in host_list:
            ip_obj = handle_mask_or_no_mask(host)
            if ip_obj:
                found_ips.append(ip_obj)
				
    return found_ips


# Does some magic to create an IP object based on inputs with our without a CIDR
def handle_mask_or_no_mask(host):
	if '/' in host:
		split_host = host.split('/')
		try:
			ip = split_host[0]
			mask_no_slash = split_host[1]
			mask_int = int(mask_no_slash)
			mask = '/' + mask_no_slash
		except:
			# cli_negative_print('Host passed in incorrect format...')
			return False
		else:
			if validate_ip(ip) and (mask_int <=32 and mask_int > 0):
				return IP(ip, mask)
				
	elif validate_ip(host):
		return IP(host)
	
	return False    

