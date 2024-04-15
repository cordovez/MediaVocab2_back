import redis

# Define the connection parameters
redis_host = "localhost"
redis_port = 6379
redis_db = 0

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# Test the connection
try:
    redis_client.ping()
    print("Redis connection successful!")
except redis.exceptions.ConnectionError:
    print("Failed to connect to Redis!")

# Set and get a test key-value pair
test_key = "test_key"
test_value = "test_value"

redis_client.set(test_key, test_value)
retrieved_value = redis_client.get(test_key)

print(f"Retrieved value for key '{test_key}': {retrieved_value.decode('utf-8')}")

# Clean up: Delete the test key
redis_client.delete(test_key)
