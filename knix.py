import os
import time
import requests
import datetime
import wget
import random
import os.path

now = datetime.datetime.now()

user = os.getlogin()

nw_dir = os.getcwd()

while True:
	usr_inp = input(f"{nw_dir}> ")
	if usr_inp == "now":
		print(f"Time: {now}")
	elif usr_inp == "cpm":
		file_inst = input("Addres to file: ") # Example https://mystat.itstep.org/assets/images/load.png?v=d39044f047d65d2db1f0e24fc47f5e6a
		wget.download(file_inst)
	elif usr_inp == "cd":
		dir_cd = input("Enter dir: ")
		if os.path.isdir(dir_cd):
			os.chdir(dir_cd)
		else:
			print("Folder don`t found.")
	elif usr_inp == "md":
		folder_cr = input("Folder name: ")
		if os.path.isdir(folder_cr):
			print("Folder already exists!")
		else:
			os.mkdir(folder_cr)
	elif usr_inp == "run_bat":
		file_run_name = input("Enter bat file name: ")
		if os.path.isfile(file_run_name):
			os.system(file_run_name)
		else:
			print("File don`t found.")
	elif usr_inp == "rd":
		folder_rm = input("Enter folder: ")
		if os.path.isdir(folder_rm):
			os.rmdir(folder_rm)
		else:
			print("Folder don`t found.")
	elif usr_inp == "editor":
		os.system("cls")
		file_name = input("Enter file name: ")
		text_inp = input("")
		file = open(file_name, "w")
		file.write(text_inp)
		file.close()
	elif usr_inp == "get_name":
		print(f"{user}")
	elif usr_inp == "rand_numbers":
		print(random.randint(0, 100))
	elif usr_inp == "clear":
		os.system("cls")
	else:
		print("Command don`t found.")