# pmeter
My first approach to achieve a Command-Line JMeter-like tool in python

I was really disappointed to know there was no easy way to use a http-pool in JMeter, and I really don't like Java at all. So I ended up making a little script that relies on Python's urllib3 http-pool to achieve this. Originally the script can lead with SOAP and HTTP servers, it's really simple and I hope to have it improved in the future. 

Requires python 2.6 + and 

Usage:
python pmeter.py -h host -t maxthreads -c cicles -p poolsize -f file -w wait -o timeout

Where: 
  - host is the target server with port
  - maxthreads is the number of threads that will be raised 
  - cicles is the number of times the threads will be sent
  - poolsize is the http-pool max number of connections, be sure to set enough for your threads
  - file is a file from where you can get random values
  - wait is the standby time between cicles
  - timeout is the max time a thread will wait for a server response
