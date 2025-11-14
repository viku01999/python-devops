import os


db_user = os.getenv('DB_USER', 'default_user')
print(db_user)

# Set an environment variable
os.environ['DB_PASSWORD'] = 'secretpassword'