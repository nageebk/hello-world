import subprocess
import os
import datetime
import time
import sys

def poll():

	is_terminal_running = False
	terminal_running_str = 'jxb'
	
	while not is_terminal_running:

		time.sleep(1)

		p = subprocess.Popen(['sudo','docker','ps'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		is_terminal_running = out.find(daemon_running_str) is not -1



# we need docker daemon
is_daemon_running = False
daemon_running_str = 'start/running'

while not is_daemon_running:
	
	log_to_file(['checking daemon availabilty'])
	time.sleep(2)

	p = subprocess.Popen(['sudo','service', 'docker', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	is_daemon_running = out.find(daemon_running_str) is not -1
	# start/running





