from includes import scan
import os

def reader(input, output=None):
    if not input:
        print("must enter the -l for file input ")

    try:
        with open(input, 'r') as file:
            for line in file:
                scan.openrescan(line.strip(), output)
    except FileNotFoundError:
            print("File not found. Check the file path and name.")