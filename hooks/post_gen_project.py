import glob
import os

gitkeep_files = glob.glob('./**/**/.gitkeep') + glob.glob('./**/.gitkeep')

for file in gitkeep_files:
	os.remove(file)


