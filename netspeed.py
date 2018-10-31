import os
import time
import sys


def get_download_bytes(line) :
	bytes_split = line.split(' ')
	while '' in bytes_split :
		bytes_split.remove('')
	downloadBytes = bytes_split[4]
	# print(downloadBytes)
	return downloadBytes



def get_bytes(text, net_card):
	start = False
	for line in text:
		if net_card in line :
			start = True
		if start :
			if 'RX packets' in line :
				download_bytes = get_download_bytes(line)
				start = False
				return int(download_bytes)


def calculate_speed(net_card) :
	while 1 :
		text = os.popen('ifconfig').readlines()
		old_bytes = get_bytes(text, net_card)
		# print(old_bytes)
		time.sleep(1)
		text = os.popen('ifconfig').readlines()
		new_bytes = get_bytes(text, net_card)
		# print(new_bytes)
		speed = round((new_bytes - old_bytes) / 1024, 2)
		# print(speed)
		sys.stdout.write(' ' * 20 + '\r')
		sys.stdout.flush()
		sys.stdout.write('Speed: {} Kb/s \r'.format(speed))


def netSpeed():
	text = os.popen('ifconfig').readlines()
	net_cards = []

	# find all net cards
	for line in text:
		if 'flags=' in line:
			tmp = line[0:line.index(': flags')]
			net_cards.append(tmp)
	
	n = 1
	select_cards = ''
	for net_card in net_cards:
		select_cards += str(n) + ':' + net_card + '\t'
		n = n + 1
	
	val = input("Select the card you want oversee!  {} \n: ".format(select_cards))

	calculate_speed(net_cards[int(val) - 1])

if __name__ == '__main__' :
	netSpeed()
