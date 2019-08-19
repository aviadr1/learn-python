import multiprocessing
import time

def do_work(name, queue, output):
	while True:
		job = queue.get()
		if job == 'END':
			break
			
		x,y, sleep = queue.get()
		time.sleep(sleep)
		output.put([name, x,y, x*y])
		
def harness():
	work = multiprocessing.Queue()
	results = multiprocessing.Queue()
	
	names = ['worker' + str(i) for i in range(100)]
	
	workers = [
		multiprocessing.Process(target=do_work, args=(name, work, results)) for name in names
	]
	
	for worker in workers:
		worker.start()
	
	jobs = []
	for i in range(1, 11):
		for j in range(1, 11):
			jobs.append( [i,j, 3] )
	
	for job in jobs:
		work.put(job)

	for worker in workers:
		work.put('END')
		
    
	while workers:
		worker = workers[-1]
		while not results.empty():
			print(results.get(0))
		if worker.join(1):
			workers.pop()
			
		
	print("All done")

if __name__ == '__main__':
	harness()
