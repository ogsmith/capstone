from controller import StandardController
import threading
import time
if __name__ == '__main__':
	threads = []
	controller = StandardController()
	loop_thread = threading.Thread(target=controller.run_loop)
	#view_thread = threading.Thread(target=controller.run_view)
	threads.append(loop_thread)
	#threads.append(view_thread)
	try:
		loop_thread.start()
		controller.run_view()
		#view_thread.start()
		print "started threads"
	except:
		print "Error: unable to start thread"
	a = 1
