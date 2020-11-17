#!/usr/bin/env python3

import argparse
import subprocess


def main(args):
	args = ['git', 'commit', '-m', args.message] + [f.name for f in args.files]
	subprocess.run(args)
	return


def add_subparser(subparsers):
	parser = subparsers.add_parser('commit')
	parser.add_argument('--message', '-m', type=str, required=True)
	parser.add_argument('files', type=argparse.FileType('r'), nargs='*')
	return

