from task import process_data

result = process_data.delay()

print(result.id)
print(result.status)
print(result.get())
