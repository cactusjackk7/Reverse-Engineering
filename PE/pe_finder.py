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
								print "Proccesing the fiel %s" % filename
				try:
								pe = pefile.PE(filename, fast_load=True)

								parts = filename.split("\\")

								shutil.copyfile(filename, join(output_dirs, parts[-1]))

				except pefile.PEFormatError:
								if verbose_mode:
												print "Skipping: file could not be read (probably a 16bit file)"

if not output_dirs:
				print "Error: Please configure the output directory"
				sys.exit(0)

for input_dirs, do_walk:
				for root, dirs, files in os.walk(input_dirs):
								for file i [ file for file in files if file_qualifies(file.lower(), input_extensions								)]:
												procces_file(join(root, file))
								else:
												for file in [file for file in os.listdir(input_dir) if file_qualifies(file.l												ower(), input_extensions)]:
																process_file(input_dir, file))

