#!/usr/bin/env python
import time
import os
try:
    red = "\033[5;49;91m"
    green = "\033[7;49;95m"
    print(f"{red}LINUX TRAVANDO!!!11!!11\033[m")
    print(f"{green}USE CONTROL + C ANTES QUE SUA MÁQUINA MORRA!\033[m")
    time.sleep(10)
    a  = [i for i in range(300_000_000)]
    for i in a:
        print(i)
        break
except:
    print("\033[3;49;94m Programa Encerrado by user!\033[m")


