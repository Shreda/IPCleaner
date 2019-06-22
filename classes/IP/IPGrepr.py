import sys
import re
from classes.IP.utils import handle_mask_or_no_mask

class IPGrepr():
    def __init__(self, filename, output):
        self.filename = filename
        self.output = output
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
            self.output.errorstdio("Input file '{}' not found...".format(self.filename))
            sys.exit()
        else:
            data = f.read()
            f.close()
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
                sys.exit()
            else:
                for addr in self.ips:
                    f.write("\n{}{}".format(addr.network_addr, addr.cidr))
        else:
            for addr in self.ips:
                print('{}{}'.format(addr.ip_addr, addr.cidr))    
