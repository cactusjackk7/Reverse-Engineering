import argparse
import imp
import marshal
import os
import struct
import time
import sys

import pefile

IGNORE = [
					'<installzipextimporter>.pyc', # zip importer added by py2exe
								]

def _timestamp():
				"""Generate timestamp data of pyc header."""
				today = time.time()
				ret = struct.pack('=L', int(today))
				return ret

def _build_magic(magic):
				"""Build Python magic number for pyc header."""
				return struct.pack('Hcc', magic, '\r', '\n')

def _current():
				"""current Python magic number. """
				return imp.get_magic()

version = {
						# version, magic (see Python/import.c)
						'1.5': __build_magic(20121),
						'1.6': __build_magic(50428),
						'2.0': __build_magic(50823),
						'2.1': __build_magic(60202),
						'2.2': __build_magic(60717),
 						'2.3': __build_magic(62011),
						'2.4': __build_magic(62061),
						'2.5': __build_magic(62131),
						'2.6': __build_magic(62161),
						'2.7': __build_magic(62191),
				}

def get_script 
