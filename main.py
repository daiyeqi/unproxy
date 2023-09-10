#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, getopt
from ipaddress import ip_interface

def main(argv):
    input_file = ''
    output_file_v4 = ''
    output_file_v6 = ''
    try:
        opts, args = getopt.getopt(argv,"i:4:6:")
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-i':
            input_file = arg
        if opt == '-4':
            output_file_v4 = arg
        if opt == '-6':
            output_file_v6 = arg
    
    fi = open(input_file, "r")
    fo4 = open(output_file_v4, "a")
    fo6 = open(output_file_v6, "a")
    try:
        lines = fi.readlines()
        for ip_address in lines:
            ip_version = ip_interface(ip_address.strip()).version
            if ip_version == 4:
                fo4.write(":do { add address=" + ip_address.strip() + " list=PROXY } on-error={}\n")
            elif ip_version == 6:
                fo6.write(":do { add address=" + ip_address.strip() + " list=PROXY } on-error={}\n")
    finally:
        fi.close()
        fo4.close()
        fo6.close()

if __name__ == "__main__":
   main(sys.argv[1:])
