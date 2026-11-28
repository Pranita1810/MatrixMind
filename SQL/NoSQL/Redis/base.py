"""Let's Build a simple redis server & client."""
import redis

# ----- REDIS SERVER CONNECTION -----
redis_server = redis.Redis(
                            host='localhost',
                            port = 6379,
                            decode_responses=True
                            )
"""Above is redis server """


# ----- REDIS CLIENT (user) -----
redis_server.set("Name", "Jagga-Daku")  
result = redis_server.get("Name")
print(result)

# -- Store & Retrieve dict --
redis_server.hset(
    'user_session',
    mapping={
        'name':'pranit',
        'company':'gen-ai',
        'age' : '24'
    }
)
result_hash = redis_server.hgetall("user_session")
print(result_hash)
redis_server.close() # -> Close the connection when the work is done



# ----- STORE DIFFERNT DATAYPES IN REDIS -----
import json
import pandas as pd

# 1. String
redis_server.set("name", "Alex")

# 2. Dictionary → Redis Hash
user = {"name": "Alex", "age": 23}
redis_server.hset("user:1", mapping=user)

# 3. List → Redis List
items = ["apple", "banana", "mango"]
redis_server.rpush("fruits", *items)

# 4. Python set → Redis Set
redis_server.sadd("cities", "Mumbai", "Pune", "Delhi")

# 5. Nested list/dict → JSON string
data = {"scores": [80, 90, 95]}
redis_server.set("data", json.dumps(data))

# 6. Pandas DataFrame → JSON string
df = pd.DataFrame({"name": ["Alex", "Sam"], "age": [23, 25]})
redis_server.set("dataframe", df.to_json(orient="records"))