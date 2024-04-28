# As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

# ●       The program should continuously monitor the CPU usage of the local machine.

# ●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

# ●       The program should run indefinitely until interrupted.

# ●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

import psutil as ps
while True:
    x =ps.cpu_percent(1)
    print (x)
    print ("Monitoring CPU usage...")
    if ps.cpu_percent() > 85:
        print("Alert! CPU usage exceeds threshold: " +  str(x) +"%" )
    else:
        print("CPU usage under threshold:  " + str(x) +"%")
