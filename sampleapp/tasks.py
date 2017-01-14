from celery.decorators import task

@task(name="sum_two_numbers")
def add(x, y):
	print 'done adding the numbers'
	return x + y
