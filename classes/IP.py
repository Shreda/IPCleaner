class IP():
    NUM_BITS_IN_OCTET = 8
    NUM_BITS_IP = 32
    NUM_BYTES_IP = 4
    MAX_OCTET_VALUE = 255

    def __init__(self, ip_addr, subnet_mask):
        self.num_hosts_network = 0
        self.ip_addr = ip_addr
        self.cidr = subnet_mask
        self.ip_addr_binary = self.ipToBinary(self.ip_addr)
        self.subnet_mask_binary = self.maskToBinary(self.cidr)
        self.network_addr_binary = self.findNetworkAddr(self.ip_addr_binary, self.subnet_mask_binary)
        self.network_addr = self.binaryToDecimal(self.network_addr_binary)
        self.subnet_mask = self.binaryToDecimal(self.subnet_mask_binary)
        self.broadcast_addr_binary = self.findBroadcastAddr(self.ip_addr_binary, self.subnet_mask_binary)
        self.broadcast_addr = self.binaryToDecimal(self.broadcast_addr_binary)
    
    def binaryToDecimal(self, binary_num):
        # print(binary_num)
        binary_octets = [binary_num[i:i+self.NUM_BITS_IN_OCTET] for i in range(0, len(binary_num), self.NUM_BITS_IN_OCTET)]
        # print(binary_octets)
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
        ip_array = []
        subnet_array = []
        network_array = []
        # print(ip_addr)
        # print(subnet_mask)
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
        print(num)
        self.num_hosts_network = num

    def findBroadcastAddr(self, ip_addr, subnet_mask):
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
        self.set_num_hosts_network(int('1'*zero_count, 2) -1)
        broadcast_addr = ''.join(broadcast_array)
        return broadcast_addr
        