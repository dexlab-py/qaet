#!/usr/bin/env python
import sys
import re
import time
import os
from getpass import getpass
from termcolor import colored
import string
import csv
import argparse

parser = argparse.ArgumentParser(description=colored('You can use qaet for Automating Qualys task with command line. There are 70 options available. You can use options.txt to see the available options.', 'green'))
args = parser.parse_args()

print'  ___      _    _____ _____ '
print' / _ \\    / \\  | ____|_   _|'
print'| | | |  / _ \\ |  _|   | |  '
print'| |_| | / ___ \\| |___  | |  '
print' \\__\\_\\/_/   \\_\\_____| |_|  '
print'                            '
print' Qulays Automation Engineering Toolkit v1.0'
print' Written by ' + colored('@Dikshant','red')
print' Contact - qaetquery@gmail.com'
print' You must need:' + colored(' username, password [Manager Role in Qalys Dashboard], Qulays Dashboard URL', 'green')
print' This script works with python [use '+ colored('chmod +x qaet.py','red')+'] before running script for linux.'
print' This sctipt works for Web Application Security Module in Qualys' + colored(' WAS ','red') +'using Qualys was API' 
print'\n'
username=getpass("Enter username :")
password=getpass("Enter Password :")
qualysurl=raw_input("Enter the URL of Qualys web dashboard :")
qualysurl=re.findall("http.*[A-Za-z0-9].com",qualysurl)
qualysurl= qualysurl[0]
qualysurl=qualysurl.replace("qualysguard","qualysapi")

connection= "curl" + " " + "-u" + " " + "\"" + username+":"+password + "\"" + " " +qualysurl +'/qps/rest/3.0/count/was/webapp'

time.sleep(2)
print '\n' + "Establishing connection.."
time.sleep(0.3)
print '\n' + "Establishing connection......"
time.sleep(0.3)
print '\n' + "Establishing connection..........."
time.sleep(0.3)
print '\n' + "Establishing connection......................"
time.sleep(0.3)
print '\n' + "Establishing connection..............................."
time.sleep(0.3)
print '\n' + "Establishing connection......................................."
time.sleep(0.3)
print '\n' + "Establishing connection................................................"
time.sleep(0.3)
print '\n' + "Establishing connection............................................................"
print '\n' + '\n'
output=os.popen(connection).read()

responseCode=re.findall("<responseCode>.*</responseCode>",output)
responseCode=responseCode[0]
responseSuccess="<responseCode>SUCCESS</responseCode>"

if responseCode == responseSuccess:
	print '\n'+"Connection Established Successfully"
else:
	print '\n'+ "Connection Not Established - Exiting" + '\n'
	exit(1)


print '\n' + "You need to select any integer number from the following options"
time.sleep(2)

def zero():
	print colored('[[+]] ','green') +"Know version of your Qualys - Selecting this option will display you the version of your Qualys. "
	try:	
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " + "-X" + " "+"\""+"GET"+"\""+ " "+ "-H" +" "+ "\""+"Accept: application/xml"+"\""+ " " +qualysurl+"/qps/rest/portal/version"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def one():
	print colored('[[+]] ','green') +"Know Number of Web Application - Selecting this option will display you total number of web applications available in your account."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "  +qualysurl+"/qps/rest/3.0/count/was/webapp"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')	

def two():
	print colored('[[+]] ','green') +"List All WEB Application - This option will list all web application under your account."
	try:	
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+  " " +qualysurl+"/qps/rest/3.0/search/was/webapp" " " + "-X" + " " + "\""+ "POST" + "\""
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')	

def three():
	print colored('[[+]] ','green') +"Deatils of one Application - This option will display details of one web application."
	try:
		webid=raw_input("Please enter the Web ID (unique) : ")
		connection=connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/webapp/" + webid
		# print connection
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')	

def four():
	print colored('[[+]] ','green') +"Details of Multiple Application - This option will display details of multiple web applications. Create a csvfile with all the web app ids [Unique ID Value]."
	try:
		id_list=raw_input("Please enter the filename with Web ID's (unique) : ")
		with open(id_list,'r') as file:
			for i in file:
				connection=connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/webapp/" + i
				# print connection
				output=os.system(connection)
				print output
	except:
		print colored("Either file is empty or you have entered wrong filename",'red')

def five():
	print colored('[[+]] ','green') +"Create One New Web Application Entry - This option will help you to create a new web application entry. Please be ready with the following details : - Please enter all the required fields"

	print colored('[[-]] ','red') + "a. Web Application Name"

	print colored('[[-]] ','red') + "b. Web Application URL"

	# print colored('[[-]] ','red') + "c. Progressive Scan - Options can be true/false"

	print colored('[[-]] ','red') + "c. How many tags need to be entered ?"

	print colored('[[-]] ','red') + "d. Enter Tag id's"

	# print colored('[[-]] ','red') + "f. Scope - Option can be All"

	print colored('[[-]] ','red') + "e. Option profile id"

	# print colored('[[-]] ','red') + "h. Authentication Record id "

	# print colored('[[-]] ','red') + "i. Scanner type - Options can be internal or external"

	# print colored('[[-]] ','red') + "j. friendly Name "
	web_name=raw_input("Enter Web Application Name: ")
	web_url=raw_input("b. Web Application URL:" )
	tag_num=int(raw_input("c. How many tags need to be entered ? -: " ) )
	tags=[None]*tag_num
	for i in range(tag_num):
		tags[i]=int(raw_input("d. Enter Tag id's:" ))
	option_profile=raw_input("e. Option profile id:" )
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()

	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+" " + " " + "<WebApp>"
	file.write(output)
	output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
	file.write(output)
	output='\n'+" " + " " + " " +"<url><![CDATA[" + web_url+"/]]></url>"
	file.write(output)
	output='\n'+" " + " " + " " +"<tags>"
	file.write(output)
	output='\n'+" " + " " + " " +" "+ "<set>"
	file.write(output)
	for i in tags:
		output='\n'+" " + " " + " " +" "+ " " +"<Tag><id>"+str(i)+"</id></Tag>"
		file.write(output)
	output='\n'+" " + " " + " " +" "+"</set>"
	file.write(output)
	output='\n'+" " + " " + " " +"</tags>"
	file.write(output)
	output='\n'+" " + " " + " " +"<defaultProfile>"
	file.write(output)
	output='\n'+" " + " " + " " +"<id>"+option_profile+"</id>"
	file.write(output)
	output='\n'+" " + " " + " " +"</defaultProfile>"
	file.write(output)
	output='\n'+" " + " " + "</WebApp>"
	file.write(output)
	output='\n'+" "+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n' +'\n'
	file.write(output)

	file.close

	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()

	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/webapp/"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
			exit(0)
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."

def six():
	print colored('[[+]] ','green') +"Create Multiple Web Applications - This option will help you to create multiple web applications enteries. Please be ready with the following details : - You can leave field needs to empty or not required or need default setting."

	print colored('[[-]] ','red') + "a. Web Application Name"

	print colored('[[-]] ','red') + "b. Web Application URL"

	print colored('[[-]] ','red') + "c. Enter Tag id's"

	print colored('[[-]] ','red') + "d. Option profile id"

	print colored('[[-]] ','red') + "Please enter all these details in a CSV. "

	print colored('[[-]] ','red') + "e.g : CSV should look like below : (Please make sure you are using the same headers as shown below ):"
	
	print colored('[[-]] ','red') + "name	webapp_url			tag_id			option_profile"

	print colored('[[-]] ','red') + "web1	https://web1.com	695556 1897585 8977586		120616"

	print colored('[[-]] ','red') + "web2	https://web2.com	695556 1897785 8977586		445522"

	print colored('[[-]] ','red') + "web3	https://web3.com	695556 1897785			775668"

	filename=raw_input("Please enter valid csv name :")
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			web_name=row[0]
			web_url=row[1]
			tags=row[2]
			option_profile=row[3]
			#remove_old_file="rm -r file.xml"
			#os.popen(remove_old_file).read()
			file = open("file.xml","w")
			output="<ServiceRequest>"
			file.write(output)
			output='\n'+"<data>"
			file.write(output)
			output='\n'+" " + " " + "<WebApp>"
			file.write(output)
			output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
			file.write(output)
			output='\n'+" " + " " + " " +"<url><![CDATA[" + web_url+"/]]></url>"
			file.write(output)
			output='\n'+" " + " " + " " +"<tags>"
			file.write(output)
			output='\n'+" " + " " + " " +" "+ "<set>"
			file.write(output)
			for i in tags.split(" "):
				output='\n'+" " + " " + " " +" "+ " " +"<Tag><id>"+str(i)+"</id></Tag>"
				file.write(output)
			output='\n'+" " + " " + " " +" "+"</set>"
			file.write(output)
			output='\n'+" " + " " + " " +"</tags>"
			file.write(output)
			output='\n'+" " + " " + " " +"<defaultProfile>"
			file.write(output)
			output='\n'+" " + " " + " " +"<id>"+option_profile+"</id>"
			file.write(output)
			output='\n'+" " + " " + " " +"</defaultProfile>"
			file.write(output)
			output='\n'+" " + " " + "</WebApp>"
			file.write(output)
			output='\n'+" "+"</data>"
			file.write(output)
			output='\n'+"</ServiceRequest>"+'\n' +'\n'
			file.write(output)
			file.close
			file=open('file.xml')
			line=file.readline()
			while line:
				print line
				line=file.readline()
				time.sleep(.1)
			file.close()

			createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
			try:
				if createwebapp.upper()=="Y":
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/webapp/"+" "+"<" +" " + "file.xml"
					output=os.system(connection) 
				else:
					print '\n'+"Exiting Program......." + '\n'
			except:
				print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def seven():
	print colored('[[+]] ','green') +"Update Web Application - for single web application - This option will help you to Edit/Modify any webapplication entry or enteries."

	print colored('[[-]] ','red') + "1. Update web application Name"

	print colored('[[-]] ','red') + "2. Update Authentication Record"

	print colored('[[-]] ','red') + "3. Cancel Scan on purticular time"

	print colored('[[-]] ','red') + "4. Update default Authentication Record for Qualys"

	print colored('[[-]] ','red') + "5. Add tag(s) for web application"

	print colored('[[-]] ','red') + "6. Remove tag(s) for web application"

	print colored('[[-]] ','red') + "7. Set new tag(s) for web applcaition "


	def a():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		web_name=raw_input("Enter New Name for Web Application : ")
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " +"<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"	
		file.write(output)
		output='\n'+" " + " " +"</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def b():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		web_name=raw_input("Enter Web Application Name: ")
		auth_id=raw_input("Enter Web Authentication Record needs to be updated: ")
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " +"<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
		file.write(output)
		output='\n'+" " + " " + " " +"<authRecords>"
		file.write(output)
		output='\n'+" " + " " + " " +"	"+" "+"<add>"
		file.write(output)
		output='\n'+" " + " " + " " +"	"+" "+"	"+"<WebAppAuthRecord>"
		file.write(output)
		output='\n'+" " + " " + " " +"	"+" "+"	"+"<id>"+auth_id+"</id>"
		file.write(output)
		output='\n'+" " + " " + " " +"	"+" "+"	"+"</WebAppAuthRecord>"
		file.write(output)
		output='\n'+" " + " " + " " +"	"+" "+"</add>"
		file.write(output)
		output='\n'+" " + " " + " " +"</authRecords>"
		file.write(output)
		output='\n'+" " + " " +"</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def c():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		web_name=raw_input("Enter Web Application Name: ")
		web_url=raw_input(" Web Application URL:" )
		cancel_time=str(raw_input(" Enter Cancel Time like e.g 22:00 " ))
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " +"<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
		file.write(output)
		output='\n'+" " + " " + " " +"<url><![CDATA[" + web_url+"></url>"
		file.write(output)
		output='\n'+" " + " " + " " +"<config><cancelScansAt>" + cancel_time+"</cancelScansAt></config>"
		file.write(output)	
		output='\n'+" " + " " +"</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def d():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		auth_record=raw_input("Please enter the Authentication Record Needs to be updated ")
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " +"<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<config>"
		file.write(output)
		output='\n'+" " + " " + " " +"<defaultAuthRecord>"
		file.write(output)
		output='\n'+" " + " " + " " + " " +"<id>"+auth_record+"</id>"
		file.write(output)
		output='\n'+" " + " " + " " +"</defaultAuthRecord>"
		file.write(output)
		output='\n'+" " + " " + " " +"<config>"
		file.write(output)
		output='\n'+" " + " " +"</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def e():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		tag_num=int(raw_input("How many tags need to be added ? -: " ) )
		tags=[None]*tag_num
		for i in range(tag_num):
			tags[i]=int(raw_input("Enter Tag id's:" ))
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " +"<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<tags>"
		file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"<add>"
		file.write(output)
		for i in tags:
			output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
			file.write(output)
			output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
			file.write(output)
			output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
			file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"</add>"
		file.write(output)
		output='\n'+" " + " " + " " +"</tags>"
		file.write(output)
		output='\n'+" " + " " +"</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."	

	def f():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		tag_num=int(raw_input("How many tags need to be removed ? -: " ) )
		tags=[None]*tag_num
		for i in range(tag_num):
			tags[i]=int(raw_input("Enter Tag id's:" ))
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " + "<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<tags>"
		file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"<remove>"
		file.write(output)
		for i in tags:
			output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
			file.write(output)
			output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
			file.write(output)
			output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
			file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"</remove>"
		file.write(output)
		output='\n'+" " + " " + " " +"</tags>"
		file.write(output)
		output='\n'+" " + " " + "</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."	
	def g():
		web_id=str(raw_input("Enter Unique web ID for updating details : (You can get it via -> WAS -> Search Web Application -> View -> ID: "))
		tag_num=int(raw_input("How many tags need to be set (This option will remove all previous tags and will set new tags ) ? -: " ) )
		tags=[None]*tag_num
		for i in range(tag_num):
			tags[i]=int(raw_input("Enter Tag id's:" ))
		#remove_old_file="rm -r file.xml"
		#os.popen(remove_old_file).read()
		file = open("file.xml","w")
		output="<ServiceRequest>"
		file.write(output)
		output='\n'+" "+"<data>"
		file.write(output)
		output='\n'+" " + " " + "<WebApp>"
		file.write(output)
		output='\n'+" " + " " + " " +"<tags>"
		file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"<set>"
		file.write(output)
		for i in tags:
				output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
				file.write(output)
				output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
				file.write(output)
				output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
				file.write(output)
		output='\n'+" " + " " + " " +" "+" "+"</set>"
		file.write(output)
		output='\n'+" " + " " + " " +"</tags>"
		file.write(output)
		output='\n'+" " + " " + "</WebApp>"
		file.write(output)
		output='\n'+" "+"</data>"
		file.write(output)
		output='\n'+"</ServiceRequest>"+'\n'
		file.write(output)
		file.close
		file=open('file.xml')
		line=file.readline()
		while line:
			print line
			line=file.readline()
			time.sleep(.1)
		file.close()
		createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
		try:
			if createwebapp.upper()=="Y":
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
				output=os.system(connection) 
			else:
				print '\n'+"Exiting Program......." + '\n'
		except:
			print '\n'+'\n'+"Something Went Wrong. Please try again......."	


	def Calloption(i):
		switcher={
				1:a,
				2:b,
				3:c,
				4:d,
				5:e,
				6:f,
				7:g,
				}
		option=switcher.get(i,lambda :'Invalid Selection')
		return option()
	select=int(raw_input('\n'+ '\n'+"Please enter your selection - anyone [1,2,3,4,5,6,7]: "+ '\n' + "-->"))
	Calloption(select)


def eight():
	print colored('[[+]] ','green') +"Update Web Application - for Multiple web applications - This option will help you to Edit/Modify any webapplication(s) entry or enteries."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file contains web application id's in one column and the required option in other column."

	print colored('[[-]] ','red') + "e.g : Below file will help you to update tag(s) for multiple web applications. "

	print colored('[[-]] ','red') + "id 			Tags"

	print colored('[[-]] ','red') + "15425		12552587"

	print colored('[[-]] ','red') + "12547		6453655 5354554 5468468 53488485"

	print colored('[[-]] ','red') + "13339		684864	8884564	54646"

	print colored('[[-]] ','red') + "1332331		4546868	888113"

	print colored('[[+]] ','green') +"Select option from below: "

	print colored('[[-]] ','red') + "1. Update web application Name"

	print colored('[[-]] ','red') + "2. Update Authentication Record"

	print colored('[[-]] ','red') + "3. Cancel Scan on purticular time"

	print colored('[[-]] ','red') + "4. Update default Authentication Record for Qualys"

	print colored('[[-]] ','red') + "5. Add tag(s) for web application"

	print colored('[[-]] ','red') + "6. Remove tag(s) for web application"

	print colored('[[-]] ','red') + "7. Set new tag(s) for web applcaition "

	def a():
		print"CSV File should look like: "
		print "web_id 				web_name"
		print "5465465				test1"
		print "5434453				test2"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and New web application name from web_name column: "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				web_name=row[1]
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " +"<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"	
				file.write(output)
				output='\n'+" " + " " +"</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def b():
		print"CSV File should look like: "
		print "web_id 				web_name		auth_id"
		print "5465465				test1			5654465"
		print "5434453				test2			5445656"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and New web application name from web_name column and Authentication ID in third column under auth_id "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				web_name=row[1]
				auth_id=row[2]
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " +"<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
				file.write(output)
				output='\n'+" " + " " + " " +"<authRecords>"
				file.write(output)
				output='\n'+" " + " " + " " +"	"+" "+"<add>"
				file.write(output)
				output='\n'+" " + " " + " " +"	"+" "+"	"+"<WebAppAuthRecord>"
				file.write(output)
				output='\n'+" " + " " + " " +"	"+" "+"	"+"<id>"+auth_id+"</id>"
				file.write(output)
				output='\n'+" " + " " + " " +"	"+" "+"	"+"</WebAppAuthRecord>"
				file.write(output)
				output='\n'+" " + " " + " " +"	"+" "+"</add>"
				file.write(output)
				output='\n'+" " + " " + " " +"</authRecords>"
				file.write(output)
				output='\n'+" " + " " +"</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def c():
		print"CSV File should look like: "
		print "web_id 				web_name		web_url					cancel_time"
		print "5465465				test1			http://test1.com 		18:00"
		print "5434453				test2			http://test2.com 		23:00"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and New web application name from web_name column and Authentication ID in third column under auth_id "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				web_name=row[1]
				web_url=row[2]
				cancel_time=row[2]
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " +"<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<name><![CDATA["+ web_name +"]]></name>"
				file.write(output)
				output='\n'+" " + " " + " " +"<url><![CDATA[" + web_url+"></url>"
				file.write(output)
				output='\n'+" " + " " + " " +"<config><cancelScansAt>" + cancel_time+"</cancelScansAt></config>"
				file.write(output)	
				output='\n'+" " + " " +"</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def d():
		print"CSV File should look like: "
		print "web_id 				auth_record"
		print "5465465				5654465"
		print "5434453				5445656"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and Authentication record in second column under auth_record : "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				auth_record=row[1]
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " +"<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<config>"
				file.write(output)
				output='\n'+" " + " " + " " +"<defaultAuthRecord>"
				file.write(output)
				output='\n'+" " + " " + " " + " " +"<id>"+auth_record+"</id>"
				file.write(output)
				output='\n'+" " + " " + " " +"</defaultAuthRecord>"
				file.write(output)
				output='\n'+" " + " " + " " +"<config>"
				file.write(output)
				output='\n'+" " + " " +"</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."

	def e():
		print"CSV File should look like: "
		print "web_id		tag_num 				tags"
		print "5465465			1					5654465"
		print "5434453			2					5445656 56465"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and number of tags on tag_num and tags need to be used :  "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				tag_num=int(row[1])
				tags=[None]*tag_num
				tags=row[2].split(" ")
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " +"<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<tags>"
				file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"<add>"
				file.write(output)
				for i in tags:
					output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
					file.write(output)
					output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
					file.write(output)
					output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
					file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"</add>"
				file.write(output)
				output='\n'+" " + " " + " " +"</tags>"
				file.write(output)
				output='\n'+" " + " " +"</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."	

	def f():
		print"CSV File should look like: "
		print "web_id		tag_num 				tags"
		print "5465465			1					5654465"
		print "5434453			2					5445656 56465"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and number of tags on tag_num and tags need to be used :  "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				tag_num=int(row[1])
				tags=[None]*tag_num
				tags=row[2].split(" ")
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " + "<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<tags>"
				file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"<remove>"
				file.write(output)
				for i in tags:
					output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
					file.write(output)
					output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
					file.write(output)
					output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
					file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"</remove>"
				file.write(output)
				output='\n'+" " + " " + " " +"</tags>"
				file.write(output)
				output='\n'+" " + " " + "</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."	
	def g():
		print"CSV File should look like: "
		print "web_id		tag_num 				tags"
		print "5465465			1					5654465"
		print "5434453			2					5445656 56465"
		filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and number of tags on tag_num and tags need to be used :  "))
		with open(filename, 'r') as csvfile:
			reader=csv.reader(csvfile)
			next(reader)
			for row in reader:
				web_id=str(row[0])
				tag_num=int(row[1])
				tags=[None]*tag_num
				tags=row[2].split(" ")
				#remove_old_file="rm -r file.xml"
				#os.popen(remove_old_file).read()
				file = open("file.xml","w")
				output="<ServiceRequest>"
				file.write(output)
				output='\n'+" "+"<data>"
				file.write(output)
				output='\n'+" " + " " + "<WebApp>"
				file.write(output)
				output='\n'+" " + " " + " " +"<tags>"
				file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"<set>"
				file.write(output)
				for i in tags:
						output='\n'+" " + " " + " " +" "+ " " +"<Tag>"
						file.write(output)
						output='\n'+" " + " " + " " +" "+ " " +" "+"<id>"+str(i)+"</id>"
						file.write(output)
						output='\n'+" " + " " + " " +" "+ " " +"</Tag>"
						file.write(output)
				output='\n'+" " + " " + " " +" "+" "+"</set>"
				file.write(output)
				output='\n'+" " + " " + " " +"</tags>"
				file.write(output)
				output='\n'+" " + " " + "</WebApp>"
				file.write(output)
				output='\n'+" "+"</data>"
				file.write(output)
				output='\n'+"</ServiceRequest>"+'\n'
				file.write(output)
				file.close
				file=open('file.xml')
				line=file.readline()
				while line:
					print line
					line=file.readline()
					time.sleep(.1)
				file.close()
				createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
				try:
					if createwebapp.upper()=="Y":
						connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/update/was/webapp/"+ web_id +" "+ " < file.xml"
						output=os.system(connection) 
					else:
						print '\n'+"Exiting Program......." + '\n'
				except:
					print '\n'+'\n'+"Something Went Wrong. Please try again......."	


	def Calloption(i):
		switcher={
				1:a,
				2:b,
				3:c,
				4:d,
				5:e,
				6:f,
				7:g,
				}
		option=switcher.get(i,lambda :'Invalid Selection')
		return option()

	select=int(raw_input('\n'+ '\n'+"Please enter your selection - anyone [1,2,3,4,5,6,7]: "+ '\n' + "-->"))
	Calloption(select)


def nine():
	print colored('[[+]] ','green') +"Delete Single Web Application - This option will help you to delete one web application from qualys records."
	web_id=str(raw_input("Please enter web application id needs to be deletd: "))

	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + "POST" + " " +qualysurl+"/qps/rest/3.0/delete/was/webapp/" + web_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def ten():
	print colored('[[+]] ','green') +"Delete Multiple Web Application - This option will help you to delete multiple web applications from qualys records."
	print colored('[[-]] ','red') + "--> Requirement - Create a file with the id's of web applications needs to be deleted."

	try:
			id_list=raw_input("Please enter the filename with Web ID's (unique) : ")
			with open(id_list,'r') as file:
				for i in file:
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + "POST" + " " +qualysurl+"/qps/rest/3.0/delete/was/webapp/" + i
					# print connection
					output=os.system(connection)
					print output
	except:
		print colored("Either file is empty or you have entered wrong filename",'red')



def eleven():
	print colored('[[+]] ','green') +"Purge one Web Application - This option will help you to purge one web application from qualys. Please enter web id :"
	try:
		web_id=str(raw_input("Please enter web application ID needs to be purged: "))
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/purge/was/webapp/" + web_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def twelve():
	print colored('[[+]] ','green') +"Purge Multiple Web Applications - This option will help you to purge multiple web applications from qualys."
	print colored('[[-]] ','red') + "--> Requirement - Create a file with the id's of web applications needs to be deleted."
	try:
			id_list=raw_input("Please enter the filename with Web ID's (unique) : ")
			with open(id_list,'r') as file:
				for i in file:
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/purge/was/webapp/" + i
					# print connection
					output=os.system(connection)
					print output
	except:
		print colored("Either file is empty or you have entered wrong filename",'red')


def thirteen():
	print colored('[[+]] ','green') +"Count Total Authentication Records - This option will help you to count the total number of Authentication records available in qualys."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/count/was/webappauthrecord/"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def fourteen():
	print colored('[[+]] ','green') +"List All Authentication Record - This option will help you to list down all the authentication records in qualys."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/search/was/webappauthrecord/"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def fifteen():
	print colored('[[+]] ','green') +"Get Authentication Records against one web application - This option will display you authentication record in qualys for one web application (if authentication record exist)"
	try:
		auth_id=raw_input("Please enter the Authentication Record id for details: ")
		connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/webappauthrecord/" + auth_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def sixteen():
	print colored('[[+]] ','green') +"Get Authentication Records for multiple web applications - This option will display you authentication records for multiple web applications (if authentication record exist)"

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of web applications."

	try:
		id_list=raw_input("Please enter the filename with Authentication Record ID's (unique) : ")
		with open(id_list,'r') as file:
			for i in file:
				connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/webappauthrecord/" + i
				output=os.system(connection)
				print output
	except:
		print colored("Either file is empty or you have entered wrong filename",'red')

def seventeen():
	print colored('[[+]] ','green') +"Create Default (Standard) Authentication Record - This option will help you to create default authentication record."

	print colored('[[-]] ','red') + "Please be ready with the following details: "

	print colored('[[-]] ','red') + "a. Name of Authentication Record"

	print colored('[[-]] ','red') + "b. WebApp Authentication Record - Username Field -"

	print colored('[[-]] ','red') + "c. WebApp Authentication Record - Password Field -"

	print colored('[[-]] ','red') + "d. Number of Tags needs to add (can be kept empty if not required ) -"

	print colored('[[-]] ','red') + "e. Enter the tags id - "

	print colored('[[-]] ','red') + "f. Comment (if required) -"

	auth_name=raw_input("Please enter Name of the Authentication Record: ")
	auth_username=raw_input("Please enter Username of the Authentication Record: ")
	auth_password=raw_input("Please enter Password of the Authentication Record: ")
	tag_num=int(raw_input("Please enter Number of Tags required for Authentication Record: "))
	tags=[None]*tag_num
	for i in range(tag_num):
		tags[i]=int(raw_input("Enter Tag id's: "))
	comment=raw_input("Please enter comment: ")
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<WebAppAuthRecord>"
	file.write(output)
	output='\n'+"<name><![CDATA["+auth_name+"]]></name>"
	file.write(output)
	output='\n'+"<formRecord>"
	file.write(output)
	output='\n'+"<type>STANDARD</type>"
	file.write(output)
	output='\n'+"<sslOnly>true</sslOnly>"
	file.write(output)
	output='\n'+"<fields>"
	file.write(output)
	output='\n'+"<set>"
	file.write(output)
	output='\n'+"<WebAppAuthFormRecordField>"
	file.write(output)
	output='\n'+"<name>username</name>"
	file.write(output)
	output='\n'+"<value>"+auth_username+"</value>"
	file.write(output)
	output='\n'+"</WebAppAuthFormRecordField>"
	file.write(output)
	output='\n'+"<WebAppAuthFormRecordField>"
	file.write(output)
	output='\n'+"<name>password</name>"
	file.write(output)
	output='\n'+"<value>"+auth_password+"</value>"
	file.write(output)
	output='\n'+"</WebAppAuthFormRecordField>"
	file.write(output)
	output='\n'+"</set>"
	file.write(output)
	output='\n'+"</fields>"
	file.write(output)
	output='\n'+"</formRecord>"
	file.write(output)
	output='\n'+"<tags>"
	file.write(output)
	output='\n'+"<set>"
	file.write(output)
	for i in tags:
		output='\n'+"<Tag>"
		file.write(output)
		output='\n'+"<id>"+str(i)+"</id>"
		file.write(output)
		output='\n'+"</Tag>"
		file.write(output)
	output='\n'+"</set>"
	file.write(output)
	output='\n'+"</tags>"
	file.write(output)
	output='\n'+"<comments>"
	file.write(output)
	output='\n'+"<set>"
	file.write(output)
	output='\n'+"<Comment><contents><![CDATA["+comment+"]]></contents></Comment>"
	file.write(output)
	output='\n'+"</set>"
	file.write(output)
	output='\n'+"</comments>"
	file.write(output)
	output='\n'+"</WebAppAuthRecord>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/webappauthrecord"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def eighteen():
	print colored('[[+]] ','green') +"Delete Authentication Record (singular) - This option will help you to delete single authentication record."
	try:
		auth_id=raw_input("Please enter the Authentication Record id needs to be deleted: ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/delete/was/webappauthrecord/"+ auth_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def nineteen():
	print colored('[[+]] ','green') +"Delete Authentication Record (Multiple) - This option will help you to delete multiple authentication records."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of authentication needs to be deleted."
	try:
		id_list=raw_input("Please enter the filename with Authentication Record ID's (unique) : ")
		with open(id_list,'r') as file:
			for i in file:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/delete/was/webappauthrecord/"+ i
				output=os.system(connection)
				print output
			file.close
	except:
		print colored("Something went wrong. Please try again",'red')

def twenty():
	print colored('[[+]] ','green') +"Count total no of scans - This option will help you to count total number of scans."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/count/was/wasscan"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def twenty_one():
	print colored('[[+]] ','green') +"View Running Scans - This option will help you to display all running scans details."

	print colored('[[-]] ','red') + "You can use custom filters - SUBMITTED, RUNNING,FINISHED, TIME_LIMIT_EXCEEDED, SCAN_NOT_LAUNCHED,SCANNER_NOT_AVAILABLE, ERROR or CANCELED"

	option=raw_input("Please enter your filter selection: ")
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"status\" operator=\"EQUALS\">"+option.upper()+"</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscan"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def twenty_two():
	print colored('[[+]] ','green') +"List scans with successful authentication - This option will help you to display all scans with successful authentication."
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"authStatus\" operator=\"EQUALS\">SUCCESSFUL</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	createwebapp=str(raw_input("This will take sometime to list all the details. Do you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscan" + " < file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def twenty_three():
	print colored('[[+]] ','green') +"List scan without any tag - This option will help you to display a list of scans without any tag."
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"webApp.tags\" operator=\"NONE\"></Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	createwebapp=str(raw_input("This will take sometime to list all the details. Do you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscan" + "< file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def twenty_four():
	print colored('[[+]] ','green') +"List scan with perticular tag - This option will help you to display a list of scans with perticular tag."
	tag_id=raw_input("Please enter the Tag id : ")
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"webApp.tags.id\" operator=\"EQUALS\">"+tag_id+"</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscan"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."		

def twenty_five():
	print colored('[[+]] ','green') +"Details of cancelled scans - This option will help you to display details of cancelled scans."
	web_id=raw_input("Please enter the web application id with cancelled scan request : ")
	#remove_old_file="rm -r file.xml"
	#os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output='\n'+"<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"id\" operator=\"IN\">"+web_id+"</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"+'\n'
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+" " + "-X" + " " + "\""+ "POST" + "\"" +" " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscan" + "<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def twenty_six():
	print colored('[[+]] ','green') +"Scan details for one web app - This option will help you to display scan details based on scan id"
	try:
		scan_id=raw_input("Please enter the scan id: ")
		connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/wasscan/" + scan_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. Please try again",'red')

def twenty_seven():
	print colored('[[+]] ','green') +"Scan details for multiple web applications - This option will help you to display scan details for multiple web applications based on scan id's. "
	filename=str(raw_input("Enter CSV filename to get scan id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			scan_id=str(row[0])
			try:
				connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/wasscan/" + scan_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')


def twenty_eight():
	print colored('[[+]] ','green') +"Launch new scan (singular) - This option will help you to initiate security scan for one web application."

	print colored('[[-]] ','red') + "Details Need to onboard application for scan : - Default would be pick if any of the details is kept empty."

	print colored('[[-]] ','red') + "a. Name of the scan"

	print colored('[[-]] ','red') + "b. Web application id"

	print colored('[[-]] ','red') + "c. Authentication record - Default"

	print colored('[[-]] ','red') + "d. ScannerType - Internal/External"

	print colored('[[-]] ','red') + "e. Option Profile id"

	print colored('[[-]] ','red') + "f. Cancel aftertime"

	print colored('[[-]] ','red') + "g. Progressive scan"

	name=raw_input("Please enter Name of the scan: ")
	web_id=raw_input("Please enter Web application id: ")
	auth_id=raw_input("Please enter Authentication record id - Default: ")
	scanner_type=raw_input("Please enter ScannerType - Internal/External: ")
	profile_id=raw_input("Please enter Option Profile id: ")
	cancel_scan_time=raw_input("Please enter Cancel aftertime, e.g Enter 5 for 5 hours: ")
	prog_scan=raw_input("Please enter if Progressive scan is required - Option Could be Enabled or Disabled: ")
	scan_type=raw_input("Please enter scan type - Option Could be DISCOVERY or VULNERABILITY: ")

	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<WasScan>"
	file.write(output)
	output='\n'+"<name>"+name+"</name>"
	file.write(output)
	output='\n'+"<type>"+scan_type.upper()+"</type>"
	file.write(output)
	output='\n'+"<target>"
	file.write(output)
	output='\n'+"<webApp>"
	file.write(output)
	output='\n'+"<id>"+web_id+"</id>"
	file.write(output)
	output='\n'+"</webApp>"
	file.write(output)
	output='\n'+"<webAppAuthRecord>"
	file.write(output)
	output='\n'+"<isDefault>true</isDefault>"
	file.write(output)
	output='\n'+"</webAppAuthRecord>"
	file.write(output)
	output='\n'+"<scannerAppliance>"
	file.write(output)
	output='\n'+"<type>"+scanner_type.upper()+"</type>"
	file.write(output)
	output='\n'+"</scannerAppliance>"
	file.write(output)
	output='\n'+"</target>"
	file.write(output)
	output='\n'+"<profile>"
	file.write(output)
	output='\n'+"<id>"+profile_id+"</id>"
	file.write(output)
	output='\n'+"</profile>"
	file.write(output)
	output='\n'+"<cancelAfterNHours>"+cancel_scan_time+"</cancelAfterNHours>"
	file.write(output)
	output='\n'+"<progressiveScanning>"+prog_scan.upper()+"</progressiveScanning>"
	file.write(output)
	output='\n'+"</WasScan>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/launch/was/wasscan"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def twenty_nine():
	print colored('[[+]] ','green') +"Launch new scan (Multiple) - This option will help you to initiate security scan for multiple web applications."

	print colored('[[-]] ','red') + "Please create a csv with the following details : - Default would be pick if any of the details is kept empty."

	print colored('[[-]] ','red') + "a. Name of the scan"

	print colored('[[-]] ','red') + "b. Type of scanning "

	print colored('[[-]] ','red') + "c. Authentication record - Default"

	print colored('[[-]] ','red') + "d. ScannerType - Internal/External"

	print colored('[[-]] ','red') + "e. Web Application ID"

	print colored('[[-]] ','red') + "f. Option Profile id"

	print colored('[[-]] ','red') + "d. Cancel aftertime"

	print colored('[[-]] ','red') + "E.g : CSV should look like below :"

	print colored('[[-]] ','red') + "name	Scantype			Authentocation		Scanner					WebID			Option Pro		Cancel Time after "

	print colored('[[-]] ','red') + "scan1	Discovery			654646846			Internal				120616			default			5	"

	print colored('[[-]] ','red') + "scan2	Vulnerability							External				12706			65466			24"

	print colored('[[-]] ','red') + "scan3																	1270336							3"

	filename=str(raw_input("Enter CSV filename to pick WebApplication id from web_id column and New web application name from web_name column: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			name=str(row[0])
			web_id=str(row[4])
			auth=str(row[2])
			scanner_type=str(row[3])
			profile_id=str(row[5])
			cancel_scan_time=str(row[6])
			scan_type=str(row[1])
			remove_old_file="rm -r file.xml"
			os.popen(remove_old_file).read()
			file = open("file.xml","w")
			output="<ServiceRequest>"
			file.write(output)
			output='\n'+"<data>"
			file.write(output)
			output='\n'+"<WasScan>"
			file.write(output)
			output='\n'+"<name>"+name+"</name>"
			file.write(output)
			output='\n'+"<type>"+scan_type.upper()+"</type>"
			file.write(output)
			output='\n'+"<target>"
			file.write(output)
			output='\n'+"<webApp>"
			file.write(output)
			output='\n'+"<id>"+web_id+"</id>"
			file.write(output)
			output='\n'+"</webApp>"
			file.write(output)
			output='\n'+"<webAppAuthRecord>"
			file.write(output)
			output='\n'+"<isDefault>true</isDefault>"
			file.write(output)
			output='\n'+"</webAppAuthRecord>"
			file.write(output)
			output='\n'+"<scannerAppliance>"
			file.write(output)
			output='\n'+"<type>"+scanner_type.upper()+"</type>"
			file.write(output)
			output='\n'+"</scannerAppliance>"
			file.write(output)
			output='\n'+"</target>"
			file.write(output)
			output='\n'+"<profile>"
			file.write(output)
			output='\n'+"<id>"+profile_id+"</id>"
			file.write(output)
			output='\n'+"</profile>"
			file.write(output)
			output='\n'+"<cancelAfterNHours>"+cancel_scan_time+"</cancelAfterNHours>"
			file.write(output)
			output='\n'+"<progressiveScanning>ENABLED</progressiveScanning>"
			file.write(output)
			output='\n'+"</WasScan>"
			file.write(output)
			output='\n'+"</data>"
			file.write(output)
			output='\n'+"</ServiceRequest>"
			file.write(output)
			file.close
			file=open('file.xml')
			line=file.readline()
			while line:
				print line
				line=file.readline()
				time.sleep(.1)
			file.close()
			createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
			try:
				if createwebapp.upper()=="Y":
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/launch/was/wasscan"+" "+"<" +" " + "file.xml"
					output=os.system(connection) 
				else:
					print '\n'+"Exiting Program......." + '\n'
			except:
				print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def thirty():
	print colored('[[+]] ','green') +"Scan Status single application - This option will help you to check the scan status for one web application. "
	try:
		scan_id=raw_input("Please enter the scan ID (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/status/was/wasscan/" + scan_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def thirty_one():
	print colored('[[+]] ','green') +"Scan Status for multiple applications - This option will help you to check the scan status for multiple web applications."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the scan id's."
	filename=str(raw_input("Enter CSV filename to get scan id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			scan_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/status/was/wasscan/" + scan_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def thirty_two():
	print colored('[[+]] ','green') +"Cancel Scan for one web application - This option will help you to cancel scan for one web application."
	try:
		scan_id=raw_input("Please enter the scan ID (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/cancel/was/wasscan/" + scan_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def thirty_three():
	print colored('[[+]] ','green') +"Cancel Scan for one multiple web applications - This option will help you to cancel scan for multiple web applications."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of scans."

	filename=str(raw_input("Enter CSV filename to get scan id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			scan_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/cancel/was/wasscan/" + scan_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def thirty_four():
	print colored('[[+]] ','green') +"Delete Scan for one web application - This option will help you to delete scan for one web application."
	try:
		scan_id=raw_input("Please enter the scan ID (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/delete/was/wasscan/" +scan_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def thirty_five():
	print colored('[[+]] ','green') +"Delete Scan for multiple web applications - This option will help you to delete scan for multiple web applications."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of scans."

	filename=str(raw_input("Enter CSV filename to get scan id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			scan_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/delete/was/wasscan/" +scan_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def thirty_six():
	print colored('[[+]] ','green') +"Never Launched Scheduled Scans - This option will give you details about the scheduled scans, which were never initiated or Launched due to some reason."
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"lastScan\" operator=\"NONE\"></Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscanschedule" +" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."


def thirty_seven():
	print colored('[[+]] ','green') +"List Lauched Schedule Scans - This option will give you list of all scans which were scheduled and were launched."
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"lastScan.status\" operator=\"IN\">FINISHED,ERROR</Criteria>"
	file.write(output)
	output='\n'+"<Criteria field=\"lastScan.launchedDate\" operator=\"LESSER\">2025-07-27</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	output='\n'+""
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/wasscanschedule"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."

def thirty_eight():
	print colored('[[+]] ','green') +"Schedule a new scan - This option will help you to schedule a new scan. Please be ready with following details :"

	print colored('[[-]] ','red') + "	a. Name of scheduled scan"

	print colored('[[-]] ','red') + "	b. type of scan - Vulnerability or Discovery "

	print colored('[[-]] ','red') + "	c. Cancel the scan after (in hours)"

	print colored('[[-]] ','red') + "	d. Occurance type - Weekly or monthly"

	print colored('[[-]] ','red') + "	e. Occurance in a month -"

	print colored('[[-]] ','red') + "	f. Which day (Monday, tuesday .... Sunday)"

	print colored('[[-]] ','red') + "	g. Web Application id"

	print colored('[[-]] ','red') + "	h. Authentication Record id "

	print colored('[[-]] ','red') + "	i. Profile id "

	name=raw_input(" Please enter Name of scheduled scan: ")
	scan_type=raw_input(" Please enter type of scan - Vulnerability or Discovery : ")
	cancel_time=raw_input(" Please enter Cancel the scan after (in hours): ")
	occurance_type=raw_input(" Please enter Occurance type - once, daily , weekly or monthly: ")
	occurance_no=raw_input(" Please enter number of Occurance in a month/week -: ")
	scan_day=raw_input(" Please enter scan day (Monday, tuesday .... Sunday): ")
	web_id=raw_input(" Please enter Web Application id: ")
	auth_id=raw_input(" Please enter Authentication Record id : ")
	prof_id=raw_input(" Please enter Profile id : ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<WasScanSchedule>"
	file.write(output)
	output='\n'+"<name><![CDATA["+name+"]]></name>"
	file.write(output)
	output='\n'+"<type>"+scan_type.upper()+"</type>"
	file.write(output)
	output='\n'+"<active>false</active>"
	file.write(output)
	output='\n'+"<scheduling>"
	file.write(output)
	output='\n'+"<cancelAfterNHours>"+cancel_time+"</cancelAfterNHours>"
	file.write(output)
	output='\n'+"<startDate>2019-09-06T09:50:11Z</startDate>"
	file.write(output)
	output='\n'+"<timeZone>"
	file.write(output)
	output='\n'+"<code>America/Vancouver</code>"
	file.write(output)
	output='\n'+"<offset>-07:00</offset>"
	file.write(output)
	output='\n'+"</timeZone>"
	file.write(output)
	output='\n'+"<occurrenceType>"+occurance_type.upper()+"</occurrenceType>"
	file.write(output)
	output='\n'+"<occurrence>"
	file.write(output)
	output='\n'+"<weeklyOccurrence>"
	file.write(output)
	output='\n'+"<everyNWeeks>2</everyNWeeks>"
	file.write(output)
	output='\n'+"<occurrenceCount>"+occurance_no+"</occurrenceCount>"
	file.write(output)
	output='\n'+"<onDays>"
	file.write(output)
	output='\n'+"<WeekDay>"+scan_day.upper()+"</WeekDay>"
	file.write(output)
	output='\n'+"</onDays>"
	file.write(output)
	output='\n'+"</weeklyOccurrence>"
	file.write(output)
	output='\n'+"</occurrence>"
	file.write(output)
	output='\n'+"</scheduling>"
	file.write(output)
	output='\n'+"<notification>"
	file.write(output)
	output='\n'+"<active>true</active>"
	file.write(output)
	output='\n'+"<reschedule>true</reschedule>"
	file.write(output)
	output='\n'+"<delay>"
	file.write(output)
	output='\n'+"<nb>1</nb>"
	file.write(output)
	output='\n'+"<scale>DAY</scale>"
	file.write(output)
	output='\n'+"</delay>"
	file.write(output)
	output='\n'+"<message><![CDATA[A Qualys scan is scheduled to start soon.]]></message>"
	file.write(output)
	output='\n'+"</notification>"
	file.write(output)
	output='\n'+"<target>"
	file.write(output)
	output='\n'+"<webApp>"
	file.write(output)
	output='\n'+"<id>"+web_id+"</id>"
	file.write(output)
	output='\n'+"</webApp>"
	file.write(output)
	output='\n'+"<webAppAuthRecord>"
	file.write(output)
	output='\n'+"<id>"+auth_id+"</id>"
	file.write(output)
	output='\n'+"</webAppAuthRecord>"
	file.write(output)
	output='\n'+"</target>"
	file.write(output)
	output='\n'+"<profile>"
	file.write(output)
	output='\n'+"<id>"+prof_id+"</id>"
	file.write(output)
	output='\n'+"</profile>"
	file.write(output)
	output='\n'+"</WasScanSchedule>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/wasscanschedule" +" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def thirty_nine():
	print colored('[[+]] ','green') +"Activate/Start/Initiate a scheduled scan - This option will help you to initiate a previously scheduled scan."
	try:
		schedule_id=raw_input("Please enter the scheduled id (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/activate/was/wasscanschedule/" + schedule_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def forty():
	print colored('[[+]] ','green') +"Activate/Start/Initiate multiple scheduled scans - This option will help you to initiate multiple previously scheduled scans."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of previously scheduled scans."

	filename=str(raw_input("Enter CSV filename to get scheduled id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			schedule_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/activate/was/wasscanschedule/" + schedule_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')


def forty_one():
	print colored('[[+]] ','green') +"Deactivate one Scheduled Scan - This option will help you to deactivate anyone previously scheduled scan."
	try:
		schedule_id=raw_input("Please enter the scheduled id (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/activate/was/wasscanschedule/" + schedule_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def forty_two():
	print colored('[[+]] ','green') +"Deactivate Multiple Scheduled scans - This option will help you to deactivate multiple previously scheduled scans."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of previously scheduled scans."

	filename=str(raw_input("Enter CSV filename to get scheduled id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			schedule_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/activate/was/wasscanschedule/" + schedule_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def forty_three():
	print colored('[[+]] ','green') +"Delete one Scheduled Scan - This option will help you to delete one previously scheduled scan."
	try:
		schedule_id=raw_input("Please enter the scheduled id (unique) : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/delete/was/wasscanschedule/" + schedule_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def forty_four():
	print colored('[[+]] ','green') +"Delete multiple Scheduled Scans - This option will help you to delete multiple previously scheduled scans."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of previously scheduled scans."

	filename=str(raw_input("Enter CSV filename to get scheduled id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			schedule_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/delete/was/wasscanschedule/" + schedule_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def forty_five():
	print colored('[[+]] ','green') +"Total no. of reports - This option will help you to display total number of reports available."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/count/was/report"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def forty_six():
	print colored('[[+]] ','green') +"List of all reports - This option will help you to display list of all reports."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " +qualysurl+"/qps/rest/3.0/search/was/report"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def forty_seven():
	print colored('[[+]] ','green') +"Search a report - This option will help you to search a report."
	report_id=raw_input("Please enter report id : ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"tags.id\" operator=\"EQUALS\">"+report_id+"</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/search/was/report"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	

def forty_eight():
	print colored('[[+]] ','green') +"Get report for one application - This option will help you to display report for one application."
	try:
		report_id=raw_input("Please enter report id: ")
		connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/report/" + report_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def forty_nine():
	print colored('[[+]] ','green') +"Get report for multiple applications - This option will help you to display report for multiple applications."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of tags with report."
	filename=str(raw_input("Enter CSV filename to get report id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			report_id=str(row[0])
			try:
				connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/report/" + report_id
				output=os.system(connection)
				print output
			except:
				print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def fifty():
	print colored('[[+]] ','green') +"Display status of report (one scan) - This option will display you the status of report for one scan."
	try:
		report_id=raw_input("Please enter report id: ")
		connection= "curl"+" "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/status/was/report/" + report_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def fifty_one():
	print colored('[[+]] ','green') +"Display status of report (multiple scans) - This option will display you the status of report for multiple scans."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with report ids."
	filename=str(raw_input("Enter CSV filename to get report id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			report_id=str(row[0])
			try:
				connection= "curl"+" "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/status/was/report/" + report_id
				output=os.system(connection)
				print output
			except:
				print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def fifty_two():
	print colored('[[+]] ','green') +"Download report for one web application - This option will help you to download report for one web application."
	try:
		report_id=raw_input("Please enter report id: ")
		connection= "curl"+" "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/download/was/report/" + report_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def fifty_three():
	print colored('[[+]] ','green') +"Download report for multiple web applications - This option will help you to download report for multiple web applications."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with report ids."
	filename=str(raw_input("Enter CSV filename to get report id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			report_id=str(row[0])
			try:
				connection= "curl"+" "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/download/was/report/" + report_id
				output=os.system(connection)
				print output
			except:
				print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')



def fifty_four():
	print colored('[[+]] ','green') +"Send encrypted report (Single) to email addresses(multiple) - This option will help you to send encrypted report to multiple email addresses."
	report_id=raw_input("Please enter report id : ")
	email_id=raw_input("Please enter the email id to send report: ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<Report>"
	file.write(output)
	output='\n'+"<distributionList>"
	file.write(output)
	output='\n'+"<add>"
	file.write(output)
	output='\n'+"<EmailAddress><![CDATA["+email_id+"]]></EmailAddress>"
	file.write(output)
	output='\n'+"</add>"
	file.write(output)
	output='\n'+"</distributionList>"
	file.write(output)
	output='\n'+"</Report>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\""  + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/send/was/report/" +report_id +" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."

def fifty_five():
	print colored('[[+]] ','green') +"Send encrypted reports (multiple) to email addresses(multiple) - This option will help you to send multiple encrypted report to multiple email addresses."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of tags with report and email_id's."
	print"--> Csv should look like below : "
	print" Report id 				email address" 
	print" 324654 					abc@abc.com"
	print" 324654 					def@abc.com"
	print" 154986 					abc@abc.com"
	print" 565564 					def@abc.com"

	filename=str(raw_input("Enter CSV filename to get report id and email addresses: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			report_id=str(row[0])
			email_id=str(row[1])
			remove_old_file="rm -r file.xml"
			os.popen(remove_old_file).read()
			file = open("file.xml","w")
			output="<ServiceRequest>"
			file.write(output)
			output='\n'+"<data>"
			file.write(output)
			output='\n'+"<Report>"
			file.write(output)
			output='\n'+"<distributionList>"
			file.write(output)
			output='\n'+"<add>"
			file.write(output)
			output='\n'+"<EmailAddress><![CDATA["+email_id+"]]></EmailAddress>"
			file.write(output)
			output='\n'+"</add>"
			file.write(output)
			output='\n'+"</distributionList>"
			file.write(output)
			output='\n'+"</Report>"
			file.write(output)
			output='\n'+"</data>"
			file.write(output)
			output='\n'+"</ServiceRequest>"
			file.write(output)
			file.close
			file=open('file.xml')
			line=file.readline()
			while line:
				print line
				line=file.readline()
				time.sleep(.1)
			file.close()
			createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
			try:
				if createwebapp.upper()=="Y":
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\""  + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/send/was/report/" +report_id +" "+"<" +" " + "file.xml"
					output=os.system(connection) 
				else:
					print '\n'+"Exiting Program......." + '\n'
			except:
				print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def fifty_six():
	print colored('[[+]] ','green') +"Delete Report (single) - This option will help you to delete single report."
	try:
		report_id=raw_input("Please enter report id: ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + qualysurl+"/qps/rest/3.0/delete/was/report/" + report_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')


def fifty_seven():
	print colored('[[+]] ','green') +"Delete report (multiple) - This option will help you to delete multiple reports."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the id's of tags with report."

	filename=str(raw_input("Enter CSV filename to get report id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			report_id=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + qualysurl+"/qps/rest/3.0/delete/was/report/" + report_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')	

def fifty_eight():
	print colored('[[+]] ','green') +"Create WAS Report (Single) - This option will help you to create a report for single web application."
	web_id=raw_input(" Please enter Web Application id: ")
	report_format=raw_input(" Please enter required format of report like PDF, XML, CSV etc : ")
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<Report>"
	file.write(output)
	output='\n'+"<name><![CDATA["+web_id+"_WAS_REPORT]]></name>"
	file.write(output)
	output='\n'+"<description><![CDATA[PDF WebApp report]]></description>"
	file.write(output)
	output='\n'+"<format>"+report_format.upper()+"</format>"
	file.write(output)
	output='\n'+"<type>WAS_WEBAPP_REPORT</type>"
	file.write(output)
	output='\n'+"<config>"
	file.write(output)
	output='\n'+"<webAppReport>"
	file.write(output)
	output='\n'+"<target>"
	file.write(output)
	output='\n'+"<webapps>"
	file.write(output)
	output='\n'+"<WebApp><id>"+web_id+"</id></WebApp>"
	file.write(output)
	output='\n'+"</webapps>"
	file.write(output)
	output='\n'+"</target>"
	file.write(output)
	output='\n'+"</webAppReport>"
	file.write(output)
	output='\n'+"</config>"
	file.write(output)
	output='\n'+"</Report>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/report"+" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def fifty_nine():
	print colored('[[+]] ','green') +"Create WAS Report (multiple) - This option will help you to create a report for multiple web applications."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the web application id."

	print"--> Csv should look like below : "
	print" Web id 					Report Format" 
	print" 324654 					xml"
	print" 324654 					PDF"
	print" 154986 					CSV"

	filename=str(raw_input("Enter CSV filename to get web id and report format: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			web_id=str(row[0])
			report_format=str(row[1])
			file = open("file.xml","w")
			output="<ServiceRequest>"
			file.write(output)
			output='\n'+"<data>"
			file.write(output)
			output='\n'+"<Report>"
			file.write(output)
			output='\n'+"<name><![CDATA["+web_id+"_WAS_REPORT]]></name>"
			file.write(output)
			output='\n'+"<description><![CDATA[PDF WebApp report]]></description>"
			file.write(output)
			output='\n'+"<format>"+report_format.upper()+"</format>"
			file.write(output)
			output='\n'+"<type>WAS_WEBAPP_REPORT</type>"
			file.write(output)
			output='\n'+"<config>"
			file.write(output)
			output='\n'+"<webAppReport>"
			file.write(output)
			output='\n'+"<target>"
			file.write(output)
			output='\n'+"<webapps>"
			file.write(output)
			output='\n'+"<WebApp><id>"+web_id+"</id></WebApp>"
			file.write(output)
			output='\n'+"</webapps>"
			file.write(output)
			output='\n'+"</target>"
			file.write(output)
			output='\n'+"</webAppReport>"
			file.write(output)
			output='\n'+"</config>"
			file.write(output)
			output='\n'+"</Report>"
			file.write(output)
			output='\n'+"</data>"
			file.write(output)
			output='\n'+"</ServiceRequest>"
			file.write(output)
			file.close
			file=open('file.xml')
			line=file.readline()
			while line:
				print line
				line=file.readline()
				time.sleep(.1)
			file.close()
			createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
			try:
				if createwebapp.upper()=="Y":
					connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/report"+" "+"<" +" " + "file.xml"
					output=os.system(connection) 
				else:
					print '\n'+"Exiting Program......." + '\n'
			except:
				print '\n'+'\n'+"Something Went Wrong. Please try again......."	



def sixty():
	print colored('[[+]] ','green') +"Count Total no of Option profiles - This option will help you to display total count of option proviles available."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/count/was/optionprofile/"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def sixty_one():
	print colored('[[+]] ','green') +"Get details of Option Profile (single) - This option will help you to display details of one option profile."
	try:
		option_profile=raw_input("Please enter option profile id: ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/optionprofile/" + option_profile
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def sixty_two():
	print colored('[[+]] ','green') +"Get details of Option Profiles (multiple) - This option will help you to display details of multiple option profiles."

	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the option profile ids."

	filename=str(raw_input("Enter CSV filename to get option profile id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			option_profile=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/optionprofile/" + option_profile
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')


def sixty_three():
	print colored('[[+]] ','green') +"Create New Option profile (Default) - This option will help you to create new option profile with default options."
	profile_name=raw_input(" Please enter the name needs to be set for option profile [Other parameters will be default]: ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<data>"
	file.write(output)
	output='\n'+"<OptionProfile>"
	file.write(output)
	output='\n'+"<name><![CDATA["+profile_name+"]]></name>"
	file.write(output)
	output='\n'+"</OptionProfile>"
	file.write(output)
	output='\n'+"</data>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" +" " + "@-" + " " +qualysurl+"/qps/rest/3.0/create/was/optionprofile/" + " "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	

def sixty_four():
	print colored('[[+]] ','green') +"Delete option profile (single) - This option will help you to delete one option profile."
	try:
		option_profile=raw_input("Please enter option profile id needs to be deleted : ")
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/delete/was/optionprofile/" + option_profile
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def sixty_five():
	print colored('[[+]] ','green') +"Delete option profile (multiple) - This option will help you to delete multiple option profiles."
	print colored('[[-]] ','red') + "--> Requirement - Create a csv file with the option profile ids."

	filename=str(raw_input("Enter CSV filename to get option profile id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			option_profile=str(row[0])
			try:
				connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/delete/was/optionprofile/" + option_profile
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')


def sixty_six():
	print colored('[[+]] ','green') +"Display total numbers of findings - This option will help you to display total count of findings."
	try:
		connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/count/was/finding/"
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def sixty_seven():
	print colored('[[+]] ','green') +"Findings for one web app - This option will help you to display count of findings based on severity."
	severity=raw_input(" Please enter the severity from 1 to 5 [Integer number] : ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"type\" operator=\"EQUALS\">VULNERABILITY</Criteria>"
	file.write(output)
	output='\n'+"<Criteria field=\"severity\" operator=\"EQUALS\">"+severity+"</Criteria>"
	file.write(output)
	output='\n'+"<Criteria field=\"status\" operator=\"IN\">NEW, ACTIVE, REOPENED</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/count/was/finding/" +" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def sixty_eight():
	print colored('[[+]] ','green') +"Findings count based on filters - This option will help you to display count of findings for based on filters."
	vuln=raw_input(" Please enter the Type - Options available VULNERABILITY, SENSITIVE_CONTENT,or INFORMATION_GATHERED: ")
	severity=raw_input(" Please enter the severity from 1 to 5 [Integer number] : ")
	status=raw_input(" Please enter the status - Options available NEW, ACTIVE, REOPENED, PROTECTED and FIXED: ")
	remove_old_file="rm -r file.xml"
	os.popen(remove_old_file).read()
	file = open("file.xml","w")
	output="<ServiceRequest>"
	file.write(output)
	output='\n'+"<filters>"
	file.write(output)
	output='\n'+"<Criteria field=\"type\" operator=\"EQUALS\">"+vuln.upper()+"</Criteria>"
	file.write(output)
	output='\n'+"<Criteria field=\"severity\" operator=\"EQUALS\">"+severity+"</Criteria>"
	file.write(output)
	output='\n'+"<Criteria field=\"status\" operator=\"IN\">"+status.upper()+"</Criteria>"
	file.write(output)
	output='\n'+"</filters>"
	file.write(output)
	output='\n'+"</ServiceRequest>"
	file.write(output)
	file.close
	file=open('file.xml')
	line=file.readline()
	while line:
		print line
		line=file.readline()
		time.sleep(.1)
	file.close()
	createwebapp=str(raw_input("Please confirm if the data is correct and you want to conntinue [Y/n]:"))
	try:
		if createwebapp.upper()=="Y":
			connection="curl" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " "+ "-H" +" "+ " " + "\"" + "content-type: text/xml" + "\""+ " " + "-X" + " " + "\""+ "POST" + "\"" + " " + "--data-binary" + " " + "@-" + " " +qualysurl+"/qps/rest/3.0/count/was/finding/" +" "+"<" +" " + "file.xml"
			output=os.system(connection) 
		else:
			print '\n'+"Exiting Program......." + '\n'
	except:
		print '\n'+'\n'+"Something Went Wrong. Please try again......."	


def sixty_nine():
	print colored('[[+]] ','green') +"Details of finding for one web app - This option will help you to display details about the finding for one web application. "
	try:
		web_id=raw_input("Please enter option web id: ")
		connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/finding/" + web_id
		output=os.system(connection)
		print output
	except:
		print colored("Something went wrong. You may have entered wrongs details. Please try again",'red')

def seventy():
	print colored('[[+]] ','green') +"Details of finding for one web app - This option will help you to display details about the finding for multiple web applications."
	filename=str(raw_input("Enter CSV filename to get option web id: "))
	with open(filename, 'r') as csvfile:
		reader=csv.reader(csvfile)
		next(reader)
		for row in reader:
			web_id=str(row[0])
			try:
				connection="curl" + " "+"-n" + " " +  "-u" + " "+ "\"" + username+":"+password + "\"" + " " +qualysurl+"/qps/rest/3.0/get/was/finding/" + web_id
				output=os.system(connection) 
			except:
				print colored("Something went wrong. Please try again",'red')

def Callfunc(i):
       switcher={
       			0:zero,
				1:one,
				2:two,
				3:three,
				4:four,
				5:five,
				6:six,
				7:seven,
				8:eight,
				9:nine,
				10:ten,
				11:eleven,
				12:twelve,
				13:thirteen,
				14:fourteen,
				15:fifteen,
				16:sixteen,
				17:seventeen,
				18:eighteen,
				19:nineteen,
				20:twenty,
				21:twenty_one,
				22:twenty_two,
				23:twenty_three,
				24:twenty_four,
				25:twenty_five,
				26:twenty_six,
				27:twenty_seven,
				28:twenty_eight,
				29:twenty_nine,
				30:thirty,
				31:thirty_one,
				32:thirty_two,
				33:thirty_three,
				34:thirty_four,
				35:thirty_five,
				36:thirty_six,
				37:thirty_seven,
				38:thirty_eight,
				39:thirty_nine,
				40:forty,
				41:forty_one,
				42:forty_two,
				43:forty_three,
				44:forty_four,
				45:forty_five,
				46:forty_six,
				47:forty_seven,
				48:forty_eight,
				49:forty_nine,
				50:fifty,
				51:fifty_one,
				52:fifty_two,
				53:fifty_three,
				54:fifty_four,
				55:fifty_five,
				56:fifty_six,
				57:fifty_seven,
				58:fifty_eight,
				59:fifty_nine,
				60:sixty,
				61:sixty_one,
				62:sixty_two,
				63:sixty_three,
				64:sixty_four,
				65:sixty_five,
				66:sixty_six,
				67:sixty_seven,
				68:sixty_eight,
				69:sixty_nine,
				70:seventy,
               }
       func=switcher.get(i,lambda :'Invalid Selection')
       return func()
time.sleep(4)

print colored('[[1]] ','blue') +" " + "- Know Number of Web Application - Selecting this option will display you total number of web applications available in your account."
print colored('[[2]] ','blue') +" " + "- List All WEB Application - This option will list all web application under your account."
print colored('[[3]] ','blue') +" " + "- Deatils of one Application - This option will display details of one web application."
print colored('[[4]] ','blue') +" " + "- Details of Multiple Application - This option will display details of multiple web applications. Create a csvfile with all the web app ids [Unique ID Value]."
print colored('[[5]] ','blue') +" " + "- Create One New Web Application Entry - This option will help you to create a new web application entry. "
print colored('[[6]] ','blue') +" " + "- Create Multiple Web Applications - This option will help you to create multiple web applications enteries."
print colored('[[7]] ','blue') +" " + "- Update Web Application - for single web application - This option will help you to Edit/Modify any webapplication entry or enteries."
print colored('[[8]] ','blue') +" " + "- Update Web Application - for Multiple web applications - This option will help you to Edit/Modify any webapplication(s) entry or enteries."
print colored('[[9]] ','blue') +" " + "- Delete Single Web Application - This option will help you to delete one web application from qualys records."
print colored('[[10]] ','blue') +" " + "- Delete Multiple Web Application - This option will help you to delete multiple web applications from qualys records."
print colored('[[11]] ','blue') +" " + "- Purge one Web Application - This option will help you to purge one web application from qualys."
print colored('[[12]] ','blue') +" " + "- Purge Multiple Web Applications - This option will help you to purge multiple web applications from qualys."
print colored('[[13]] ','blue') +" " + "- Count Total Authentication Records - This option will help you to count the total number of Authentication records available in qualys."
print colored('[[14]] ','blue') +" " + "- List All Authentication Record - This option will help you to list down all the authentication records in qualys."
print colored('[[15]] ','blue') +" " + "- Get Authentication Records against one web application - This option will display you authentication record in qualys for one web application (if authentication record exist)"
print colored('[[16]] ','blue') +" " + "- Get Authentication Records for multiple web applications - This option will display you authentication records for multiple web applications (if authentication record exist)"
print colored('[[17]] ','blue') +" " + "- Create Default (Standard) Authentication Record - This option will help you to create default authentication record."
print colored('[[18]] ','blue') +" " + "- Delete Authentication Record (singular) - This option will help you to delete single authentication record."
print colored('[[19]] ','blue') +" " + "- Delete Authentication Record (Multiple) - This option will help you to delete multiple authentication records."
print colored('[[20]] ','blue') +" " + "- Count total no of scans - This option will help you to count total number of scans."
print colored('[[21]] ','blue') +" " + "- View Running Scans - This option will help you to display all running scans details."
print colored('[[22]] ','blue') +" " + "- List scans with successful authentication - This option will help you to display scans with successful authentication."
print colored('[[23]] ','blue') +" " + "- List scan without any tag - This option will help you to display a list of scans without any tag."
print colored('[[24]] ','blue') +" " + "- List scan with perticular tag - This option will help you to display a list of scans with perticular tag.  "
print colored('[[25]] ','blue') +" " + "- Details of cancelled scans - This option will help you to display all details of cancelled scans."
print colored('[[26]] ','blue') +" " + "- Scan details for one web app - This option will help you to display scan details for one web application."
print colored('[[27]] ','blue') +" " + "- Scan details for multiple web applications - This option will help you to display scan details for multiple web applications. "
print colored('[[28]] ','blue') +" " + "- Launch new scan (singular) - This option will help you to initiate security scan for one web application."
print colored('[[29]] ','blue') +" " + "- Launch new scan (Multiple) - This option will help you to initiate security scan for multiple web applications."
print colored('[[30]] ','blue') +" " + "- Scan Status single application - This option will help you to check the scan status for one web application. "
print colored('[[31]] ','blue') +" " + "- Scan Status for multiple applications - This option will help you to check the scan status for multiple web applications."
print colored('[[32]] ','blue') +" " + "- Cancel Scan for one web application - This option will help you to cancel scan for one web application."
print colored('[[33]] ','blue') +" " + "- Cancel Scan for one multiple web applications - This option will help you to cancel scan for multiple web applications."
print colored('[[34]] ','blue') +" " + "- Delete Scan for one web application - This option will help you to delete scan for one web application."
print colored('[[35]] ','blue') +" " + "- Delete Scan for multiple web applications - This option will help you to delete scan for multiple web applications."
print colored('[[36]] ','blue') +" " + "- Never Launched Scheduled Scans - This option will give you details about the scheduled scans, which were never initiated or Launched due to some reason."
print colored('[[37]] ','blue') +" " + "- List Lauched Schedule Scans - This option will give you list of all scans which were scheduled and were launched."
print colored('[[38]] ','blue') +" " + "- Schedule a new scan - This option will help you to schedule a new scan. Please be ready with following details :"
print colored('[[39]] ','blue') +" " + "- Activate/Start/Initiate a scheduled scan - This option will help you to initiate a previously scheduled scan."
print colored('[[40]] ','blue') +" " + "- Activate/Start/Initiate multiple scheduled scans - This option will help you to initiate multiple previously scheduled scans."
print colored('[[41]] ','blue') +" " + "- Deactivate one Scheduled Scan - This option will help you to deactivate anyone previously scheduled scan."
print colored('[[42]] ','blue') +" " + "- Deactivate Multiple Scheduled scans - This option will help you to deactivate multiple previously scheduled scans."
print colored('[[43]] ','blue') +" " + "- Delete one Scheduled Scan - This option will help you to delete one previously scheduled scan."
print colored('[[44]] ','blue') +" " + "- Delete multiple Scheduled Scans - This option will help you to delete multiple previously scheduled scans."
print colored('[[45]] ','blue') +" " + "- Total no. of reports - This option will help you to display total number of reports available."
print colored('[[46]] ','blue') +" " + "- List of all reports - This option will help you to display list of all reports."
print colored('[[47]] ','blue') +" " + "- Search a report - This option will help you to search a report."
print colored('[[48]] ','blue') +" " + "- Get report for one application - This option will help you to display report for one application."
print colored('[[49]] ','blue') +" " + "- Get report for multiple applications - This option will help you to display report for multiple applications."
print colored('[[50]] ','blue') +" " + "- Display status of report (one scan) - This option will display you the status of report for one scan."
print colored('[[51]] ','blue') +" " + "- Display status of report (multiple scans) - This option will display you the status of report for multiple scans."
print colored('[[52]] ','blue') +" " + "- Download report for one web application - This option will help you to download report for one web application."
print colored('[[53]] ','blue') +" " + "- Download report for multiple web applications - This option will help you to download report for multiple web applications."
print colored('[[54]] ','blue') +" " + "- Send encrypted report (Single) to email addresses(multiple) - This option will help you to send encrypted report to multiple email addresses."
print colored('[[55]] ','blue') +" " + "- Send encrypted report (multiple) to email addresses(multiple) - This option will help you to send multiple encrypted report to multiple email addresses."
print colored('[[56]] ','blue') +" " + "- Delete Report (single) - This option will help you to delete single report."
print colored('[[57]] ','blue') +" " + "- Delete report (multiple) - This option will help you to delete multiple reports."
print colored('[[58]] ','blue') +" " + "- Create WAS Report (Single) - This option will help you to create a report for single web application."
print colored('[[59]] ','blue') +" " + "- Create WAS Report (multiple) - This option will help you to create a report for multiple web applications."
print colored('[[60]] ','blue') +" " + "- Count Total no of Option profiles - This option will help you to display total count of option proviles available."
print colored('[[61]] ','blue') +" " + "- Get details of Option Profile (single) - This option will help you to display details of one option profile."
print colored('[[62]] ','blue') +" " + "- Get details of Option Profiles (multiple) - This option will help you to display details of multiple option profiles."
print colored('[[63]] ','blue') +" " + "- Create New Option profile (Default) - This option will help you to create new option profile with default options."
print colored('[[64]] ','blue') +" " + "- Delete option profile (single) - This option will help you to delete one option profile."
print colored('[[65]] ','blue') +" " + "- Delete option profile (multiple) - This option will help you to delete multiple option profiles."
print colored('[[66]] ','blue') +" " + "- Display total numbers of findings - This option will help you to display total count of findings."
print colored('[[67]] ','blue') +" " + "- Findings for one web app - This option will help you to display findings for one web application."
print colored('[[68]] ','blue') +" " + "- Findings for Multiple web apps - This option will help you to display findings for multiple web applications."
print colored('[[69]] ','blue') +" " + "- Details of finding for one web app - This option will help you to display details about the finding for one web application. "
print colored('[[70]] ','blue') +" " + "- Details of finding for one web app - This option will help you to display details about the finding for multiple web applications."

select=int(raw_input('\n'+ '\n'+" Enter your option : please select valid integer number "+ '\n' + "-->"))
Callfunc(select)
