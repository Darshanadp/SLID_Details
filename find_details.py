#Find Details from SLID Number

# import numbers 0 to 9 for checking id number validation
import string
numbers = list(string.digits)

# import date and time 
import datetime

# Assign months for calculation
months = {31:'Janurary', 60:'February', 91:'March', 121:'April', 152:'May', 182:'June', 213:'July', 244:'August', 274:'September', 305:'October', 335:'November', 366:'December'}
sign_month = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]


# Guide lines
print('''Use SLID Card Number to get the details of the owner 
Please Enter fully ID Card Number with x and v if it's old ID Card
''')


# Input user id number
def inp():
	global id_num ## list of the numbers in id card
	
	value = (input('Enter ID Card Number : '))
	if value.lower() == 'exit': 	## when type exit programm will EXIT
		exit()
	id_num = list(value)
	vali() 				## calling to 'Check ID Number Validation'
	
# Check ID Number Validation	
def vali():
	global ve  ## version of the id card 'old or new'
	
	## Checking the id number status 'Old or New'
	if len(id_num) == 10 and (id_num[-1].lower() in ['v','x']):
		ve = 'Old' 		## version value is set to 'Old'
		k = 9
	elif len(id_num) == 12 :
		ve = 'New' 		## version value is set to 'New'
		k = 12
	else : 
		error() 		## calling to 'Error Message'
		return
		
	
	## Check all the characters are in number format
	for a in id_num[0:k]:
		if a in numbers :
			found_all = True
		else :
			found_all = False
			break
	
	## Finalizing of checking id number validation.
	if ve == 'Old' and found_all == True :
		old() 			# calling to 'Old_number year calc'
	elif ve == 'New' and found_all == True :
		new() 			# calling to 'New_number year calc'
	else :
		error()			# callting to 'Error message'
		return




# Calculation #

## Old_number year calc
def old():
	global b_yy
	b_yy = 1900 + (int(id_num[0]) * 10 + int(id_num[1]))
	cal(2) 				# calling to 'Calculation except year'


## New_number year calc
def new():
	global b_yy
	b_yy = int(id_num[0]) * 1000 + int(id_num[1]) * 100 + int(id_num[2]) * 10 + int(id_num[3])
	cal(4) 				# calling to 'Calculation except year'


## Calculation except year
def cal(s):
	
	### Month & Date calculation
	def gender(g):
		MM = (int(id_num[s]) - (5 * g))* 100 + int(id_num[s+1]) * 10 + int(id_num[s+2]) 
		if not MM <= 366 :
			error()
			return()
		else : 
			for i in range(1,14):
				if MM < sign_month[i-1] :
					global b_mm
					global y
					y = sign_month[i-1]
					b_mm = months[y]
					break
		global b_dd
		b_dd = MM - sign_month[i-2]
		
		global a_yy
		now_year = datetime.datetime.now().year
		a_yy = now_year - b_yy
		
		out() # callint to 'Display outputs'
		
	### Gender calculation
	global gen
	if int(id_num[s]) >= 5 :
		gen = 'Female'
	else :
		gen = 'Male'
	
	
	### Check ability of voting
	global vote
	if gen == 'Female' : 
		per = 'She'
	else :
		per = 'He'	
	
	### Addressing the person according to gender
	if id_num[-1].lower() == 'v' and ve == 'Old' :
		vote = f'{per} has the ability to vote in a government election'
	elif id_num[-1].lower() == 'x' and ve == 'Old' :
		vote = f'{per} can NOT vote in a government election'
	else :
		vote = 'Unknown'
	
	
	### Finalizing gender and call to the function
	if gen == 'Female' :
		gender(1)	# calling to 'Month Calculation' for female ID
	else : 
		gender(0)	# calling to 'Month Calculation' for male ID
		
	


# Display outputs
def out():
	print('')
	print(f'Year of birth  	: {b_yy}')
	print(f'Month of birth 	: {b_mm}')
	print(f'Date of birth  	: {b_dd}')
	print(f'Gender 		: {gen}')
	print(f'Age 		: {a_yy}')
	print(f'Vote Status 	: {vote}')
	print(f'ID Card Version	: {ve}')


# Error Message
def error():
	print('Wrong ID Number Check again !!\nOR type exit to stop program\n')
	inp() # calling to 'Input` user id number'


inp() # calling to 'Input user id number' to start Program as first command




