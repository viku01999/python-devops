cpu = 4
ram = 16
print(cpu + ram)

print(cpu > 2)

is_linux = True
is_prod = False
print(is_linux and not is_prod)


cpu_threshold = 80
if cpu_threshold > 75:
    print("CPU usage high! Consider scaling up.")