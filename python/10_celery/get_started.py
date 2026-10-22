from get_started_task import addition

result = addition.delay(10, 20)

print(result.id)  # Task ID
print(result.status)  # Usually PENDING 
print(result.get())