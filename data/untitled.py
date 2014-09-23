import sys, os

if len(sys.argv) > 1:
	folder = sys.argv[1]

files = os.listdir(folder)

ids = sorted(set(map(lambda file: int(file.split('.')[0]), files)))