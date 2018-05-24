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
usage: IPCleaner.py [-h] [-o \<output-file-name\>] [-q] \<input-file-name\>

positional arguments:
  \<input-file-name\>     Input list of line seperated IP addresses

optional arguments:
  -h, --help            show this help message and exit
  -o \<output-file-name\>, --output \<output-file-name\>
                        Output file
  -q, --quite           Output IP addresses only (Use when piping output)

## Examples 
1. You have a file (Perhaps output from another tool) called input.txt that you want to extract IP addresses from and output to a file called hosts.txt\

  ./IPCleaner.py input.txt -o hosts.txt

2. You have a list of IP addresses which you want to sort and print to STDOUT to pipe the output into another command

./IPCleaner.py unsorted_hosts.txt -q | cut ...

