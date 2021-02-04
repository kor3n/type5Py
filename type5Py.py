import time, multiprocessing
from passlib.hash import md5_crypt

# Used to crack or test security of your cisco type 5 passwords
# V1.0 03/02/2021

line_num = 0
current_pass = '$1$5df7$Zl8LxVtuLT.qANdcQzlgE1'

# open wordlist
def readfilez():
	with open('shortlist.txt') as x:
		filez = x.read()
	return filez

# convert to cisco type5 and compare to see if correct
def cisco_type5(listGroup):
	for text in listGroup:
		if md5_crypt.verify(text, current_pass):
			print('[+] - {}'.format(text))			
			return True

def main():
    # list size for big word list
	lSize = 5000
    
    # make the file into a list
	pwList = readfilez().splitlines()
	
    # splits into smaller lists from the lSize variable
	man_pwList = [pwList[i:i + lSize] for i in range(0, len(pwList),lSize)]
	
    # holder for the Processes
	multi_pro = []
	
    # basic multiprocessing adding to the holder and stating them
	for group in man_pwList:
		p = multiprocessing.Process(target=cisco_type5, args=[group])
		multi_pro.append(p)
		p.start()

	# holding the program until the multiprocessing process are finished
	for process in multi_pro:
		process.join()
		
	
# basic stuff with a timer to state how long it took in seconds
if __name__ == "__main__":
	try:
		start_time = time.perf_counter()
		print('\n')
		main()
		print('\n\n')
		finish_time = time.perf_counter()
		print('[+] - Time to run was {} second(s)'.format(round(finish_time-start_time, 2)))
		print('[+] - The number of lines that where iterated where: {}'.format(line_num))
	except:
		finish_time = time.perf_counter()
		print('[+] - Time to run was {} second(s)'.format(round(finish_time-start_time, 2)))
		print('[+] - The number of lines that where iterated where: {}'.format(line_num))
		print('[!] - Script Errored\n\n')
		raise