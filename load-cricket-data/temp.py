import certifi
import ssl
import urllib3

# Set the path for SSL certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Update urllib3 to use this SSL context
urllib3.PoolManager(ssl_context=ssl_context)

# import sys
# print(sys.path)
