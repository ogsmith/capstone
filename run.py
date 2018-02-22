from controller import StandardController
import threading
import time
threads = []
if __name__ == '__main__':
	controller = StandardController()
	loop_thread = threading.Thread(target=controller.run_loop)
	view_thread = threading.Thread(target=controller.run_view)
	threads.append(loop_thread)
	threads.append(view_thread)
	try:
		view_thread.start()
		time.sleep(3)
		loop_thread.start()
		print "started threads"
	except:
		print "Error: unable to start thread"
	a = 1