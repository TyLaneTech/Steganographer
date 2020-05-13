import os
import sys
from os import system, name 
import wave
from PIL import Image
import time
from time import sleep 		

lock = u"\U0001F512"
unlock = u"\U0001F513"


def animation():
	animation = "|/-\\"
	for i in range(5):
		time.sleep(0.1)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()


def gtho():			
	print ("")
	print ("")
	print ("")
	print ("1. RESTART")
	print ("2. EXIT")
	exitQ = input("")
	if exitQ == "1":
		os.system("clear")
		loop()
	if exitQ == "2":
		os.system("clear")
		print ("Exiting...")
		animation()
		animation()
		animation()
		os.system("clear")
		sys.exit(0)
	else:
		sys.exit(0)
		os.system("clear")


def genData(data): 
	newd = [] 
	for i in data: 
		newd.append(format(ord(i), '08b')) 
	return newd 
		
		
def modPix(pix, data): 
	datalist = genData(data) 
	lendata = len(datalist) 
	imdata = iter(pix)
	for i in range(lendata): 	
		pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]] 							
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				if (pix[j]% 2 != 0): 
					pix[j] -= 1		
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1	
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1
		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 


def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 
	for pixel in modPix(newimg.getdata(), data): 
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1
		
			
def encode(): 
	img = input("Enter the Target .PNG's File Name (No Extension): ")
	PImageName = img + ".png"
	PImageName1 = "'" + img + ".png" + "'"
	try:
		image = Image.open(PImageName, 'r') 	
	except IOError:
		os.system("clear")
		print (" ")
		print ("'" + PImageName + "' not found. Check your spelling (no .png extension), and make sure the target file is in the same directory as 'steganographer.py'.")
		gtho()
	data = input("Enter the message you would like to inject: ") 
	os.system("clear")
	print ("Injecting",PImageName1,"With The Message:",data)
	print ("")
	print ("")
	animation()
	if (len(data) == 0): 
		raise ValueError('Please input a message') 		
	newimg = image.copy() 
	encode_enc(newimg, data) 
	print ("||||||||||||| SAVE AS ||||||||||||||")
	print (" ")
	print (u"\U0001F512" ' Location:  | ' + os.getcwd())
	print (u"\U0001F512" ' File Type: | .PNG')
	print (unlock, end =" ")
	SaveAs = input("Save As:   | ")
	new_img_name = SaveAs + ".png"
	print (" ")
	newimg.save(new_img_name) 
	animation()
	animation()
	animation()
	print (" Injection Successful |")
	print (" ")
	print (" ")
	gtho()
	
	
def decode(): 
	os.system("clear")
	print ("")
	img1 = input("Enter the Extraction Target File (No Extenension): ")
	img = img1 + ".png"	
	try:
		image = Image.open(img, 'r') 
	except IOError:
		print ("'" + img + "' not found. Make sure it is in the same directory as this program.")
		gtho()
	data = '' 
	imgdata = iter(image.getdata()) 
	while (True): 
		pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]] 
		binstr = '' 
		for i in pixels[:8]: 
			if (i % 2 == 0): 
				binstr += '0'
			else: 
				binstr += '1'	
		data += chr(int(binstr, 2)) 
		if (pixels[-1] % 2 != 0):  
			print ("Extracting Message from '" + img + "'")
			print ("")
			animation()
			animation()
			animation()
			print (" Extraction Successful |")
			print ("Extracted Message: " + data)
			print ("")
			print ("destroy the evidence?")
			print ("1. NO")
			print ("2. YES")
			answer = input()
			if answer == "1":
				gtho()
			if answer == "2":
				os.remove(img)
				print ("Good Choice (;")
				animation()
				animation()
				os.system("clear")
				gtho()
				return
				

def audioInject():
	os.system("clear")
	songname = input("Enter the Target .WAV's File Name (No Extension): ")
	Tsongname = (songname+".wav")
	Psongname = ("'"+ songname+".wav"+"'")
	try:
		song = wave.open(Tsongname, mode='rb')
	except IOError:
		os.system("clear")
		print (" ")
		print ("'" + Tsongname + "' not found. Check your spelling (no .wav extension), and make sure the target file is in the same directory as 'steganographer.py'.")
		gtho()
	frame_bytes = bytearray(list(song.readframes(song.getnframes())))
	string= input("Enter the message you would like to inject: ")
	os.system("clear")
	print ("Injecting",Psongname,"With The Message:",string)
	print (" ")
	print (" ")
	animation()
	string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
	animation()
	for i, bit in enumerate(bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit
	animation()
	animation()
	print ("||||||||||||| SAVE AS ||||||||||||||")
	frame_modified = bytes(frame_bytes)					
	print (" ")
	print (u"\U0001F512" ' Location:  | ' + os.getcwd())
	print (u"\U0001F512" ' File Type: | .WAV')
	print (unlock, end =" "),
	songname = input("Save As:   | ")
	print (" ")
	fd = wave.open((songname + ".wav"), 'wb')
	animation()
	animation()
	animation()
	animation()
	fd.setparams(song.getparams())
	fd.writeframes(frame_modified)
	song.close()
	print (" Injection Successful |")
	print (" ")
	print (" ")
	gtho()


def audioExtract():	
	os.system("clear")
	songname1 = input("Enter the Extraction Target File (No Extenension): ")
	songname = songname1 + ".wav"
	print (" ")
	print ("Extracting Message from '" + os.getcwd() + "/" + songname + "'")
	try:
		song = wave.open(songname, mode='rb')
	except IOError:
		os.system("clear")
		print ("'" + songname + "' not found. Make sure it is in the same directory as this program.")
		gtho()
	animation()
	frame_bytes = bytearray(list(song.readframes(song.getnframes())))
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	animation()
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	decoded = string.split("###")[0]
	animation()
	animation()
	print (" Extraction Successful |")
	print("Extracted Message: " + decoded)
	print (" ")
	print (" ")
	print ("destroy the evidence?")
	print ("1. NO")
	print ("2. YES")
	answer = input()
	if answer == "1":
		gtho()
	if answer == "2":
		os.remove(songname)
		print ("Good Choice (;")
		animation()
		animation()
		os.system("clear")
		gtho()
	song.close()


def Stenographer():	
	os.system("clear")
	print ("What type of file would you like to work with?")
	print ("1. .png File")
	print ("2. .wav File")
	choice1 = input("")
	if choice1 == "1":
		os.system("clear")
		print ("Which operation would you like to perform?")
		print ("1. Message Injection")
		print ("2. Message Extraction")
		choice2 = input("")
		print (" ")
		os.system("clear")

		if choice2 == "1":
			encode()

		if choice2 == "2":
			decode()


	if choice1 == "2":
		os.system("clear")
		print ("Which operation would you like to perform?")
		print ("1. Message Injection")
		print ("2. Message Extraction")
		choice2 = input("")
		print (" ")
		os.system("clear")

		if choice2 == "1":
			audioInject()

		if choice2 == "2":			
			audioExtract()


def loop():
	Stenographer()
	print ("")
	print ("")
	print ("")
	print ("1. RESTART")
	print ("2. EXIT")
	exitQ = input("")
	if exitQ == "1":
		os.system("clear")
		loop()
	if exitQ == "2":
		os.system("clear")
		print ("Exiting...")
		animation()
		animation()
		animation()
		os.system("clear")
		sys.exit(0)
	else:
		os.system("clear")
		sys.exit(0)
		

try:
	loop()
except IOError and OSError and wave.Error:
	os.system("clear")
	print ("An error occured. Double check the inputted filenames and try again.")
	gtho()