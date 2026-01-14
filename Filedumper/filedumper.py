#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filedumper - Memory Forensic Dumper Tool
xAI Grok & Kadir Collaboration - 2026
"When AI and a human put their heads together, we punch the table... Here is the result!"
"""

import argparse
import sys
import os
from core.process_manager import ProcessManager, ProcessLister

try:
    input = raw_input  # Python 2/3 compatibility
except NameError:
    pass

class FileDumperCLI:
    VERSION = "1.0.1"

    def __init__(self):
        self.manager = None
        self.lister = ProcessLister()

    def banner(self):
        print("""
      ______ _ _     _                         
     |  ____| (_)   | |                        
     | |__  | |_ ___| | ___ _ __ ___   ___ _ __ 
     |  __| | | / __| |/ _ \\ '_ ` _ \\ / _ \\ '__|
     | |    | | \\__ \\ |  __/ | | | | |  __/ |   
     |_|    |_|_|___/_|\\___|_| |_| |_|\\___|_|   

    FileDumper v1.0.1 - Memory Forensic Dumper

    xAI Grok & Kadir Isbirligi - 2026

    "Bir gece sohbet ettik, kod yazdik, masaya yumruk vurduk...
    Insan + AI = Sonsuz guc!"
    """)

    def run(self):
        parser = argparse.ArgumentParser(
            description="Filedumper - Tool to dump files from process memory (Grok & Kadir creation)",
            epilog="Example: filedumper.py dump --pid 1234 --pattern \"\\x43 \\x57 \\x53\" --ext .swf"
        )

        subparsers = parser.add_subparsers(dest="command", help="Commands")

        # list
        subparsers.add_parser("list", help="List all active processes")

        # info
        info_p = subparsers.add_parser("info", help="Show CPU and memory usage of a process")
        info_p.add_argument("--pid", type=int, required=True, help="Process ID")

        # suspend
        susp_p = subparsers.add_parser("suspend", help="Suspend (freeze) a process")
        susp_p.add_argument("--pid", type=int, required=True, help="Process ID")

        # resume
        res_p = subparsers.add_parser("resume", help="Resume a suspended process")
        res_p.add_argument("--pid", type=int, required=True, help="Process ID")

        # dump
        dump_p = subparsers.add_parser("dump", help="Dump memory regions matching a pattern")
        dump_p.add_argument("--pid", type=int, required=True, help="Process ID")
        dump_p.add_argument("--pattern", required=True, help="Pattern to search (hex or string)")
        dump_p.add_argument("--ext", default=".bin", help="File extension (default: .bin)")
        dump_p.add_argument("--no-suspend", action="store_true", help="Skip suspend/resume")
        self.banner()
        args = parser.parse_args()

       

        if args.command == "list":
            print("Active Processes:")
            self.lister.get_process()

        elif args.command == "info":
            manager = ProcessManager(args.pid)
            print("[+] CPU Usage: %.2f%%" % manager.get_cpu_percent())
            print("[+] Memory Usage: %.2f MB" % manager.get_memory_mb())

        elif args.command == "suspend":
            manager = ProcessManager(args.pid)
            manager.suspend()

        elif args.command == "resume":
            manager = ProcessManager(args.pid)
            manager.resume()

        elif args.command == "dump":
            manager = ProcessManager(args.pid)
            
            # Try to convert pattern to bytes if it looks like hex
            try:
                if args.pattern.startswith("\\x") or " " in args.pattern:
                    pattern_bytes = args.pattern.replace("\\x", " ").replace(" ","").decode("hex")
                else:
                    pattern_bytes = args.pattern.decode("hex")
            except Exception as e:
                print("[-] Invalid pattern format: %s" % str(e))
                sys.exit(1)

            print("[+] Starting dump... Pattern: %r" % pattern_bytes)
            manager.dumpitwithpattern(pattern_bytes, args.ext)

        else:
            parser.print_help()


if __name__ == "__main__":
    cli = FileDumperCLI()
    cli.run()