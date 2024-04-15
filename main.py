import os
import argparse

parser = argparse.ArgumentParser(prog='IA_redownloader', description='Program that tries to redownload files that that failed to download from internet archive')
parser.add_argument('-log', type=str, default='log.txt', help="Filename of ia's logs")
parser.add_argument('-ia_args', type=str, default='', help="additional arguments to pass to ia command")
args = parser.parse_args()

file = open(args.log, "r")
ia_log = file.read()
file.close()
ia_log = ia_log.splitlines()

for line in ia_log:
    if line.endswith("errors"):
        filename = line.split(':')[0]
        os.system(f"ia download {filename} {args.ia_args}")
