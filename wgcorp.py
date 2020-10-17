import os, sys, time, random
os.system("clear")
def intro():
	l = '''

********************************
*	WGCORP250 AUTO BOT     *
********************************

'''
	earn = "0.00"
	print(l)
	u = input("Username: ")
	p = input("Password: ")
	print("\nPlease wait...")
	time.sleep(2)
	os.system("clear")
	print(l)

def stat():
	laga()
	#os.system("clear")
	time.sleep(1)
	print("Your Slot Code: GIAREG22810671")
	print("Your Wallet: PHP 0.00")
	print("Total Earned:", var)
	print("Your Captcha Points:", var)
	print("Total Captcha Points Earned:", var)

	
def status():
	print("Your Slot Code: GIAREG22810671")
	print("Your Wallet: PHP 0.00")
	print("Total Earned: 0.00")
	print("Your Captcha Points: 0.00")
	print("Total Captcha Points Earned: 0.00")


def laga():
	ll = '''

********************************
*	WGCORP250 AUTO BOT     *
********************************

'''
	print(ll)
	
def menu():
	
	lo = '''

[1] START CAPTCHA
[2] EXCHANGE POINTS

'''
	print(lo)

	select = input("Select [1-2]: ")
	if select == "1":
		time.sleep(1)
		os.system("clear")
		time.sleep(2)
		magic()
		pts()
		os.system("clear")
		stat()
		con()
	elif select == "2":
		print("please wait...")
	
	else:
		print("Input error, please try again")

	

def con():
	#os.system("clear")
	logos = '''
	
	[1] CONTINUE CAPTCHA
	[2] Exit
	
	'''
	print (logos)
	response = input("select [1-2]: ")
	if response == '1':
		stat()
		menu()
		
	elif response == '2':
		os.system("python wgcorp.py")
		
	else:
		print("invalid input!")
		
		
def pts():
	earn = random.randint(230, 300)
	return earn
var = pts()
add = var + var
	
def magic():
	print("\n\nAutomating....\n")
	time.sleep(1)
	for i in range(5):
		s = random.choice(['35 ==> 5 x 7', '9 ==> 8 + 1', '120 ==> 115 + 5', '7 ==> 7 x 1', '100 ==> 91 + 9'])
		r = random.randint(1,99999)
		ra = random.choice([s, r])
		print(ra)
		time.sleep(1)

intro()
status()
menu()	
	
