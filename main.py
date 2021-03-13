from ethermine import Ethermine
from time import time, sleep
import logging

ethermine = Ethermine()

wallet = "0xFb61515607a3756BF3146812B80CD147ac67D6a8"

workers = ["bobo", "buco", "petrik"]

logs = {}

for worker in workers:
    logs[worker] = open(f"{worker}.log", "a+")

while True:
    for worker in workers:
        try:
            stats = ethermine.miner_worker_current_stats(wallet, worker)
            logs[worker].write(f"{stats['validShares']}\n")
            logs[worker].flush()
            print(str(stats["validShares"]))
        except KeyError as e:
            logging.error(e)
    sleep(120)
