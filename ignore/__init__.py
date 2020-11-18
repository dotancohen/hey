#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

def get_git_root():
	process_args = ['git', 'rev-parse', '--show-toplevel']
	try:
		gitdir = subprocess.check_output(process_args).strip()
	except subprocess.CalledProcessError as e:
		print("Not in a repository.", file=sys.stderr)
		return None

	return gitdir.decode('utf8')


def get_ignore_file():
	filename = get_git_root() + '/.gitignore'
	ignorefile = open(filename, 'a+')
	return ignorefile


def main(args):
	
	ignorefile = get_ignore_file()
		
	for f in args.files:
		# TODO: Check if file in .gitignore before adding!
		relpath = os.path.relpath(f.name, get_git_root())
		ignorefile.write(relpath + "\n")

	return


def add_subparser(subparsers):
	parser = subparsers.add_parser('ignore')
	parser.add_argument('files', help="Files to ignore", type=argparse.FileType('r'), nargs='+')
	return

