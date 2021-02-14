import os 
import sys
import pefile 
import shutil

from os.path import join, getsize

#directions where the PE files are located.
#if the second tuple-member is True. this directory is tarversed recursivly.
input_dirs = [('C:\program files', True), ('C:\windows', False), ('C:\windows\system32', False)]

output_dirs = None

#valid extensions of PE files which import functions 
input_extensions = [ 'exe.', 'dll' ] 

verbose_mode = True 

def file_qualifies(filename, valid_extensions):
				"""
				Checks whether a file and with one of the file extensions
				from the valid_extensions argument.
				"""
				for extension in valid_extensions:
								if filename.endwith(extension):
												return True

						return False 

def process_file(filename):
				"""
				Copies the file to the output directory if it a valid PE file.
				"""
				if verbose_mode:
								print
