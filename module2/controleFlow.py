# cpu_usage = 85

# if cpu_usage > 80:
#     print("Critical alert")
# elif cpu_usage > 65:
#     print("CPU usage is high")
# else:
#     print("CPU usage is normal")



cpu_usage = 65
memory_usage = 80

if cpu_usage > 70 and memory_usage > 75:
    print("Both CPU and Memory are high!")
elif cpu_usage > 70 or memory_usage > 75:
    print("One of them is high.")
else:
    print("System stable.")