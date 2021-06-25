#!/usr/bin/env python3
import shutil
import psutil

#Verifica se o espaço livre é superior a 20%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
#Verifica se o uso de cpu ´e maior que 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("everthing ok!")