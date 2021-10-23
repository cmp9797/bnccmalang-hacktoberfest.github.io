from __future__ import print_function
import os, sys, time, json, random, requests

def clearConsole():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")

def runningText(text):
	for i in text + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(random.random() * 0.4)

def showBanner():
	banner = """ _   _  ___    _         ___    _   _  _____  ___   _____  ___    _   _  ___    ___   
( ) ( )|  _`\\ ( )       (  _`\\ ( ) ( )(  _  )|  _`\\(_   _)(  _`\\ ( ) ( )(  _`\\ |  _`\\ 
| | | || (_) )| |       | (_(_)| |_| || ( ) || (_) ) | |  | (_(_)| `\\| || (_(_)| (_) )
| | | || ,  / | |  _    `\\__ \\ |  _  || | | || ,  /  | |  |  _)_ | , ` ||  _)_ | ,  / 
| (_) || |\\ \\ | |_( )   ( )_) || | | || (_) || |\\ \\  | |  | (_( )| |`\\ || (_( )| |\\ \\ 
(_____)(_) (_)(____/'   `\\____)(_) (_)(_____)(_) (_) (_)  (____/'(_) (_)(____/'(_) (_)
                                                                                      
	> Credit :
		- Instagram : @syauqqii
		- Telegram  : @syauqqii

	> Source API :
		- Link	: https://hadi-api.herokuapp.com/api/

	> Menu   :
		[1] bit.ly       [3] cutt.ly      [5] Exit
		[2] shorturl.at  [4] tinyurl.com
	"""
	print(banner)

def bitLy(link):
	url = f"https://hadi-api.herokuapp.com/api/bitly?url={link}"
	req = requests.get(url).text
	res = json.loads(req)
	if res['status'] == 200:
		print(f"\n	> Hasil  : {res['result']}")
	else:
		print(f"\n> Error  : {res['msg']}")
	lanjut()

def shortUrl(link):
	url = f"https://hadi-api.herokuapp.com/api/shorturl?url={link}"
	req = requests.get(url).text
	res = json.loads(req)
	if res['status'] == 200:
		print(f"\n	> Hasil  : {res['result']}")
	else:
		print(f"\n> Error  : {res['msg']}")
	lanjut()

def cuttLy(link):
	url = f"https://hadi-api.herokuapp.com/api/cuttly?url={link}"
	req = requests.get(url).text
	res = json.loads(req)
	if res['status'] == 200:
		print(f"\n	> Hasil  : {res['result']}")
	else:
		print(f"\n> Error  : {res['msg']}")
	lanjut()

def tinyUrl(link):
	url = f"https://hadi-api.herokuapp.com/api/tinyurl?url={link}"
	req = requests.get(url).text
	res = json.loads(req)
	if res['status'] == 200:
		print(f"\n	> Hasil  : {res['result']}")
	else:
		print(f"\n> Error  : {res['msg']}")
	lanjut()

def lanjut():
	lanjut = input("\n	> Lanjutkan program (y/n) ? ")
	lanjut = str.upper(lanjut)
	if lanjut == "Y":
		clearConsole()
		noLoad()
	# elif lanjut == "n" or "N":
	else:
		exit()

def noLoad():
	clearConsole()
	showBanner()
	try:
		pilih = int(input("> Pilih  : "))
	except:
		clearConsole()
		print("[!] Error: Input harus angka !")
		time.sleep(1)
		exit()
	if pilih == 1:
		link = input("	> Link   : ")
		bitLy(str(link))
	elif pilih == 2:
		link = input("	> Link   : ")
		shortUrl(link)
	elif pilih == 3:
		link = input("	> Link   : ")
		cuttLy(link)
	elif pilih == 4:
		link = input("	> Link   : ")
		tinyUrl(link)
	elif pilih == 5:
		clearConsole()
		exit()
	else:
		clearConsole()
		print("[!] Error: pilihan anda tidak ada dalam menu !")
		time.sleep(1)
		exit()

def main():
	clearConsole()
	print("[*] ", end='')
	runningText("Starting Program ...")
	time.sleep(1)
	clearConsole()
	showBanner()
	try:
		pilih = int(input("	> Pilih  : "))
	except:
		clearConsole()
		print("[!] Error: Input harus angka !")
		time.sleep(1)
		exit()
	if pilih == 1:
		link = input("	> Link   : ")
		bitLy(str(link))
	elif pilih == 2:
		link = input("	> Link   : ")
		shortUrl(link)
	elif pilih == 3:
		link = input("	> Link   : ")
		cuttLy(link)
	elif pilih == 4:
		link = input("	> Link   : ")
		tinyUrl(link)
	elif pilih == 5:
		clearConsole()
		exit()
	else:
		clearConsole()
		print("[!] Error: pilihan anda tidak ada dalam menu !")
		time.sleep(1)
		exit()

if __name__ == '__main__':
	try:
		main()
	except:
		clearConsole()
		exit()
