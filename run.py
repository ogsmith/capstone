from controller import StandardController
import threading

if __name__ == '__main__':
	threads = []
	controller = StandardController()
	loop_thread = threading.Thread(target=controller.run_loop)
	loop_thread.setDaemon(True)
	threads.append(loop_thread)
	try:
		loop_thread.start()
		controller.run_view()
		print "Started threads"
	except:
		print "Error: unable to start thread"
