import argparse
from utils import banner
from includes import scan
from includes import readfile
from utils import check_inter


def banner_h():
    banner.display_help()


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-u", '--url', type=str, help="URL to scan")
parser.add_argument("-l", '--input', type=str, help="lost of input file")
parser.add_argument("-o", '--output', type=str, help="output in text file")
parser.add_argument("-h", "--help", action="store_true", help="Help menu")

args = parser.parse_args()

if args.help:
    banner.display_help()
if args.url and not args.output:
    banner.banner()
    scan.openrescan(args.url)
if args.input or args.output:
    banner.banner()
    readfile.reader(args.input,args.output)
    



if __name__ == "__main__":
    if check_inter.check_internet():
         pass
    else:
        print("Check Internet Connection")

