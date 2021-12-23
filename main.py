import numpy
from graphical import realTimePlot
import subprocess, threading, time

RANGE = '20.20.17.'
timeMax = 1.5
threadsMax = 255

xLabels = list(range(1, threadsMax))
timeOfIps = numpy.multiply(numpy.ones(len(xLabels)), 0)

class ParallelPing(threading.Thread):
    def __init__(self, id, timeMax):
        threading.Thread.__init__(self)
        self.id = id
        self.timeMax = timeMax

    def run(self):
        result = subprocess.run(['./getTime.sh', RANGE+str(self.id)], stdout=subprocess.PIPE)
        try:
            y = float(result.stdout.decode("utf-8"))
            #if y > self.timeMax:
            #    y = self.timeMax
        except:
            y = 0
        timeOfIps[self.id-1] = (y + timeOfIps[self.id-1]) / 2.

threads = [None] * threadsMax
line1 = []
while True:
    for ip in range(1,255):
        threads[ip-1] = ParallelPing(ip, timeMax)
        threads[ip-1].start()
    line1 = realTimePlot(xLabels, timeOfIps, line1, 'Ping gráfico')
    time.sleep(1)
input()