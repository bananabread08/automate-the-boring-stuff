import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# to disable logging, uncomment code below
# logging.disable(logging.CRITICAL)


logging.debug('Start')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    
    #if(n == 0):
    #    return 1
    #for i in range(1, n + 1):

    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))
    return total

print(factorial(1))
print(factorial(0))
print(factorial(5))

logging.debug('End')

# fix: add condition if n = 0 to return 1 and make range start at 0.
