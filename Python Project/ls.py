import os, sys, time, random

def run(text):
	for i in text + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(random.random() * 0.000000001)

def main():
	os.system("cls")
	file_path = [os.path.abspath(x) for x in os.listdir()]
	print("\n [#] List of directory : ")
	root2 = file_path[0].split(":")
	print(f" [#] Disk   : {root2[0]} \n")
	for i in range(len(file_path)):
		exc = file_path[i].split("\\")
		print("  > ", end='')
		run(exc[-1])

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print()
		sys.exit()
