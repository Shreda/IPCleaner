from optparse import OptionParser, OptionGroup

class ArgumentParser(object):
    def __init__(self):
        options = self.parseArgs()
        self.input = options.input
        self.output= options.output
        self.calc = options.calc
        self.sort = options.sort
        self.unique = options.unique
        self.quite = options.quite


    def parseArgs(self):
        parser = OptionParser()
        calc = OptionGroup(parser, 'Calculation settings')
        search = OptionGroup(parser, 'Search Settings')
        general = OptionGroup(parser, 'General Settings')
        # Search options
        search.add_option(
            '-i', 
            '--input', 
            help='File to extract IP addresses from',
            action='store',
            type='string',
        )
        search.add_option(
            '-o', 
            '--output', 
            help='Output file',
            action='store',
            type='string',
        )
        search.add_option(
            '-s',
            '--sort',
            help='Sort output',
            action='store_true'
        )
        search.add_option(
            '-u',
            '--unique',
            help='Remove duplicate IP addresses',
            action='store_true'
        )

        # IPCalculator options
        calc.add_option(
            '-c',
            '--calc',
            help='Calculate network information for an IP',
            action='store',
            type='string'
        )

        # General options
        general.add_option(
            '-q',
            '--quite',
            help='Reduce stdio ouput',
            action='store_true',
        )

        parser.add_option_group(search)
        parser.add_option_group(calc)
        parser.add_option_group(general)
        options, arguments = parser.parse_args()
        return options        