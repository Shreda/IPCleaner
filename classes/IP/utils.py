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

