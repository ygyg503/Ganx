#!/usr/bin/python
#-*-coding:utf-8-*-
#版本一:把一个文件夹备份为zip格式并且文件夹附带创建时间
#version2.0 update: 增加了备份文件夹,增加备份格式tar.gz

import os
import time

def backup(source,path = "./",ways = "zip"):
	backup_time = time.strftime("%H:%M:%S")
	backup_type = ".zip"
	
	#creat a dir and name with y/m/d
	if os.path.exists(path) == True:
		path = path + time.strftime("%y_%m_%d")
		if os.path.exists(path) == False:
			os.mkdir(path) 
			print path
	else:
		print "Backup Path Error !"

	#the final target backup file path
	backup_time = time.strftime("%H:%M:%S")
	if ways == "zip":
		backup_type = ".zip"
	elif ways == "tar.gz":
		backup_type = ".tar.gz"
	else:
		backup_type = ".tar.bz2"
	target_name = path + "/" + "backup_" + backup_time + backup_type

	#tell use if succees or error.
	def backup_command(command):
		if command == 0:
			print "Succeed Backup File !"
		else:
			print "Backup Error !"
			print command

	#choose the backup ways
	if ways == "zip":
		x = os.system("zip -qr %s %s" % (target_name,source))
		backup_command(x)
	elif ways == "tar.gz":
		x = os.system("tar -czvf %s %s" % (target_name,source))
		backup_command(x)
	elif ways == "tar.bz2":
		x = os.system("tar -cjvf %s %s" % (target_name,source))
		backup_command(x)	

if __name__ == "__main__":
	backup("backup.py","./","tar.bz2")	
