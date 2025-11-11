# def say_hello():
#     print("Hello python")

# say_hello()



# def greet_user(name):
#     print(f"Welcome, {name}")

# greet_user("Vikas")



# def sum_numbers(a, b):
#     return a+b

# result = sum_numbers(5, 10)
# print(result)


# def defult_parameters(env = "dev"):
#     print(f"Current env is {env}")

# defult_parameters()





# def resource_summary(cpu, ram, storage):
#     return cpu, ram, storage

# c, r, s = resource_summary(10,35,20)
# print(f"The data is  {c, r, s}")




def check_server_health(cpu_usage, memory_usage):
    if(cpu_usage > 80 or memory_usage > 80):
        return "High usage"
    else:
        return "Healthy"
    
print(check_server_health(80,90))