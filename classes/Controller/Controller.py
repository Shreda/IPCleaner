from classes.IP.IPGrepr import IPGrepr
from classes.IP.utils import handle_mask_or_no_mask

class Controller():
    def __init__(self, arguments, output):
        self.args = arguments
        self.output = output
        self.banner()

        if self.args.input:
            input_file_name=self.args.input
            output_file_name = self.args.output
            grepr = IPGrepr(input_file_name, self.output)
            grepr.grep()

            if len(grepr.ips) > 0:
                if self.args.sort:
                    grepr.sort()
                if self.args.unique:
                    grepr.unique()
                if self.args.output:
                    grepr.write(output_file_name)

                else:
                    grepr.write()

            else:	
                output.errorstdio("No IP addresses found.")

        elif self.args.calc:
            input_host = self.args.calc
            ip_obj = handle_mask_or_no_mask(input_host)
            if ip_obj:
                print(ip_obj)
            else:
                output.errorstdio('Not a valid IP address...')

        else:
            pass

    def banner(self):
	# Prints the programs banner, usually the most important step.
	    if not self.args.quite:
		    print(
'''
  _____ _____   _____ _                            
 |_   _|  __ \ / ____| |                           
   | | | |__) | |    | | ___  __ _ _ __   ___ _ __ 
   | | |  ___/| |    | |/ _ \/ _` | '_ \ / _ \ '__|
  _| |_| |    | |____| |  __/ (_| | | | |  __/ |   
 |_____|_|     \_____|_|\___|\__,_|_| |_|\___|_|  
 v0.1
'''
)
