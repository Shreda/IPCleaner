import sys
import re
from classes.IP.utils import handle_mask_or_no_mask

class IPGrepr():
    def __init__(self, filename):
        self.filename = filename
        self.ips = []

    def grep(self):
        '''
        Takes a file as input and uses a regular expression to find regular IP addresses with or without a CIDR.
        From this, it creates IP objects and returns them in a list.
        '''
        found_ips = []
        try:
            f=open(self.filename, "r")
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
                    
        self.ips = found_ips

    def sort(self):
        '''
        Takes a list of IP objects as input sorts them and returns them.
        '''
        self.ips.sort(key=lambda s: list(map(int, s.ip_addr.split('.'))))

    def unique(self):
        '''
        Takes a list of IP objects as input and removes duplicate entries based on
        the stored ip_addr string.
        '''
        unique_host_list = []
        unique_host_objects = []

        for host in self.ips:
            host_ip = host.ip_addr
            if host_ip not in unique_host_list:
                unique_host_list.append(host_ip)
                unique_host_objects.append(host)
            
        self.ips = unique_host_objects

    def write(self, outputfile=False):
        '''
        Take an optional file as input and writes the output to a file or stdio.
        '''
        if outputfile:
            try:
                f = open(outputfile, "w+")
            except:
                # cli_negative_print('Unable to create file to write output...')
                sys.exit()
            else:
                # cli_plus_print("Writing IPs to {}".format(output_file_name))
                for addr in self.ips:
                    f.write("\n{}{}".format(addr.network_addr, addr.cidr))
        else:
            for addr in self.ips:
                print('{}{}'.format(addr.ip_addr, addr.cidr))    
