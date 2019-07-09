# IPCleaner
```
  _____ _____   _____ _                            
 |_   _|  __ \ / ____| |                           
   | | | |__) | |    | | ___  __ _ _ __   ___ _ __ 
   | | |  ___/| |    | |/ _ \/ _` | '_ \ / _ \ '__|
  _| |_| |    | |____| |  __/ (_| | | | |  __/ |   
 |_____|_|     \_____|_|\___|\__,_|_| |_|\___|_|  
 
 ```
A tool for finding IP Adressses in a file as well as sorting IPs and removing duplicates.

## Usage
```
Usage: IPCleaner.py [options]

Options:
  -h, --help            show this help message and exit

  Search Settings:
    -i INPUT, --input=INPUT
                        File to extract IP addresses from
    -o OUTPUT, --output=OUTPUT
                        Output file
    -s, --sort          Sort output
    -u, --unique        Remove duplicate IP addresses

  Calculation settings:
    -c CALC, --calc=CALC
                        Calculate network information for an IP

  General Settings:
    -q, --quite         Reduce stdio ouput

  Expansion settings:
    -e EXPAND, --expand=EXPAND
                        Print all addresses in a network
```

## Examples 
1. You have a file (Perhaps output from another tool) called input.txt that you want to extract IP addresses from and output to a file called hosts.txt
```
./IPCleaner.py --input input.txt --output hosts.txt --sort --unique
```
2. You have a list of IP addresses which you want to sort and print to STDOUT to pipe the output into another command
```
./IPCleaner.py --input unsorted_ips.txt --sort | cut ... | grep
```
3. You want to calculate network information for the 192.168.1.0/28 network
```
./IPCleaner.py --calc 192.168.1.0/28

  _____ _____   _____ _                            
 |_   _|  __ \ / ____| |                           
   | | | |__) | |    | | ___  __ _ _ __   ___ _ __ 
   | | |  ___/| |    | |/ _ \/ _` | '_ \ / _ \ '__|
  _| |_| |    | |____| |  __/ (_| | | | |  __/ |   
 |_____|_|     \_____|_|\___|\__,_|_| |_|\___|_|  
 v0.1

IP Address:         192.168.1.0      11000000101010000000000100000000  
Subnet Mask:        255.255.255.240  11111111111111111111111111110000  
Network Address:    192.168.1.0      11000000101010000000000100000000  
Broadcast Address:  192.168.1.15     11000000101010000000000100001111  
Num Hosts:          14  
```

4. You want to print all IP addresses in a network
```
./IPCleaner.py --expand 192.168.1.10/24

192.168.1.0
192.168.1.1
192.168.1.2
...
...
192.168.1.255
```
