#!/usr/bin/env python3

import argparse
import subprocess


def main(args):
	process_args = ['git', 'init']
	subprocess.run(process_args)
	return


def add_subparser(subparsers):
	parser = subparsers.add_parser('init')
	return

