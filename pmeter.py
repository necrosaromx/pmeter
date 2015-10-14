from urllib3 import HTTPConnectionPool
import threading
import time
import logging
import sys, getopt
import random
import xml.etree.ElementTree as ET

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, pool, file_name, time_out):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.pool = pool
        self.file_name = file_name
        self.time_out = time_out
    def run(self):
        logging.info('%s Comenzando ...', self.name)
        #print_time(self.name, self.counter, 5)
        logging.info('%s Generando request ', self.name)
        msisdn = random.choice(list(open(file_name)))
        logging.info('%s El msisdn de consulta es %s', self.name, msisdn)
        profile_option = ['PRE', 'POS', 'MIX']
        roaming_option = ['0', '1', '2', '3']
        profile = (random.choice(profile_option))
        roaming = (random.choice(roaming_option))
        start_time = time.time()
        full_uri = '/balance/?profile=' + profile + '&roaming=' + roaming
        r = self.pool.urlopen('GET', full_uri, headers={'x-nokia-msisdn':msisdn.rstrip()}, timeout = float(self.time_out))
        logging.info('%s Tomo  \033[1;31m %s segundos \033[0m' , self.name, (time.time() - start_time))        
        #print r.data
        logging.info ('Saliendo %s', self.name)
try:
    opts, args = getopt.getopt(sys.argv[1:],"h:t:c:p:f:w:o:")
    logging.debug('Esto es opts %s', opts)
    logging.debug('Esto es args %s', args)
except getopt.GetoptError:
    print sys.argv[0] + ' -h host -t threads  -c cicles -p poolsize -f archivo -w espera -o timeout'
    sys.exit(2)
logging.debug('Argumentos %s', args)
for opt, arg in opts:
    if opt == "-h":
        logging.debug('El host es %s', arg)
        host = arg
    elif opt == "-t":
        logging.debug('Los threads son  %s', arg)
        thread_num = arg
    elif opt == "-c":
        logging.debug('Los ciclos son  %s', arg)
        ciclos = arg
    elif opt == "-p":
        logging.debug('El tamano del pool es  %s', arg)
        poolsize = arg
    elif opt == "-f":
        logging.debug('Archivo es  %s', arg)
        file_name = arg
    elif opt == "-w":
        logging.debug('La espera es  %s', arg)
        wait_sec = arg
    elif opt == "-o":
        logging.debug('El timeout es  %s', arg)
        time_out = arg

logging.info('Direccion host: %s', host)
#logging.info('Direccion host: %s', sys.argv[1])
#p = HTTPConnectionPool(sys.argv[1], maxsize=100)
p = HTTPConnectionPool(host, maxsize=int(poolsize))


for i in range(1, int(ciclos) + 1 ):
        for j in range(1,int(thread_num) +1 ):
            thread = myThread(j, "Thread-"+str(i)+"-"+str(j),j, p, file_name, time_out)
            thread.start()
            #La siguiente condicion espera el thread para continuar....
            # if thread.isAlive():
            #     thread.join()
        logging.info('Esperando %s segundos...', wait_sec)
        time.sleep(int(wait_sec))




print "Exiting Main Thread"
sys.exit()

