class IP():
    # The number of bits in a single IP octet
    NUM_BITS_IN_OCTET = 8
    # The number of bits in a single IP address
    NUM_BITS_IP = 32
    # The number of bytes in a single IP address
    NUM_BYTES_IP = 4
    # Largest value for 8 bits is 255
    MAX_OCTET_VALUE = 255

    def __init__(self, ip_addr, cidr='/32'):
        self.num_hosts_network = 1
        self.ip_addr = ip_addr
        self.cidr = cidr
        self.ip_addr_binary = self.ipToBinary(self.ip_addr)
        
        self.subnet_mask_binary = self.maskToBinary(self.cidr)
        self.network_addr_binary = self.findNetworkAddr(self.ip_addr_binary, self.subnet_mask_binary)
        self.network_addr = self.binaryToDecimal(self.network_addr_binary)

        self.subnet_mask = self.binaryToDecimal(self.subnet_mask_binary)
        
        self.broadcast_addr_binary = self.findBroadcastAddr(self.ip_addr_binary, self.subnet_mask_binary)
        self.broadcast_addr = self.binaryToDecimal(self.broadcast_addr_binary)
    
    def binaryToDecimal(self, binary_num):
        binary_octets = [binary_num[i:i+self.NUM_BITS_IN_OCTET] for i in range(0, len(binary_num), self.NUM_BITS_IN_OCTET)]
        decimal_octets = []
        for octet in binary_octets:
            decimal_octets.append(str(int(octet, 2)))
        ip_addr = '.'.join(decimal_octets)
        return ip_addr

    def ipToBinary(self, ip_addr):
        octets = ip_addr.split('.')
        octet_list = []

        for octet in octets:
            octet_int = int(octet)
            binary = "{0:b}".format(octet_int)
            num_missing_zeros = self.NUM_BITS_IN_OCTET - len(binary)
            complete_octet = '0'*num_missing_zeros + binary
            octet_list.append(complete_octet)

        binary_ip = ''.join(octet_list)
        return binary_ip

    def maskToBinary(self, subnet_mask):
        if '/' in subnet_mask:
            num_bits = int(subnet_mask.split('/')[1])
            num_missing_zeros = self.NUM_BITS_IP - num_bits
            binary_mask = '1'*num_bits + '0'*num_missing_zeros
            
            return binary_mask

    def findNetworkAddr(self, ip_addr, subnet_mask):
        '''
        Given a particular IP address and subnet mask (in binary format), calculates the network address.
        For example: The IP/CIDR 192.168.1.1/24 would have the following network address -> 192.168.1.0.

        The network address, is the first address in a particular subnet and cannot be used for hosts.
        '''
        ip_array = []
        subnet_array = []
        network_array = []

        for x in range(len(ip_addr)):
            ip_array.append(ip_addr[x])
            subnet_array.append(subnet_mask[x])

        for i in range(len(ip_array)):
            if subnet_array[i] == '0':
                network_array.append('0')

            else:
                network_array.append(ip_array[i])
        
        network_addr = ''.join(network_array)
        return network_addr

    def set_num_hosts_network(self, num):
        self.num_hosts_network = num

    def findBroadcastAddr(self, ip_addr, subnet_mask):
        '''
        Given a particular IP address and subnet mask, calculates the broadcast address of the network.
        For example: The IP/CIDR 192.168.1.1/24 would have the following broadcast address -> 192.168.1.255.

        The broadcast address is the last address in a subnet and is used to address all hosts.
        '''
        ip_array = []
        subnet_array = []
        broadcast_array = []
        zero_count = 0

        for x in range(len(ip_addr)):
            ip_array.append(ip_addr[x])
            subnet_array.append(subnet_mask[x])

        for i in range(len(ip_array)):
            if subnet_array[i] == '0':
                broadcast_array.append('1')
                zero_count += 1
            else:
                broadcast_array.append(ip_array[i])
        if zero_count > 0:
            self.set_num_hosts_network(int('1'*zero_count, 2) -1)
        broadcast_addr = ''.join(broadcast_array)
        return broadcast_addr

    def set_cidr(self, cidr):
        self.cidr = cidr

    def set_ip_addr(self, ip_string):
        pass

    def __str__(self):
        s = ""
        s += '{:<19} {:<16} {:<34}\n'.format('IP Address:', self.ip_addr, self.ip_addr_binary)
        s += '{:<19} {:<16} {:<34}\n'.format('Subnet Mask:', self.subnet_mask, self.subnet_mask_binary)
        s += '{:<19} {:<16} {:<34}\n'.format('Network Address:', self.network_addr, self.network_addr_binary)
        s += '{:<19} {:<16} {:<34}\n'.format('Broadcast Address:', self.broadcast_addr, self.broadcast_addr_binary)
        s += '{:<19} {:<16}'.format('Num Hosts:', self.num_hosts_network)
        return s
        