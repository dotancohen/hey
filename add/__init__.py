#!/usr/bin/env python3

import argparse
import subprocess


def main(args):
	process_args = ['git', 'add'] + [f.name for f in args.files]
	subprocess.run(process_args)
	return


def add_subparser(subparsers):
	parser = subparsers.add_parser('add')
	parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
	return

