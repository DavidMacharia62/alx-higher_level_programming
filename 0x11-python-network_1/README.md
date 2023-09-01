# Using Python to Fetch and Manipulate Internet Resources

In this README, we will cover various aspects of fetching and manipulating internet resources using Python. We will explore two popular libraries for making HTTP requests: `urllib` and `requests`. Additionally, we will see how to handle responses, fetch JSON resources, and manipulate data from external services.

## Table of Contents
1. [Fetching Internet Resources with urllib](#fetching-internet-resources-with-urllib)
2. [Decoding urllib Body Response](#decoding-urllib-body-response)
3. [Using the requests Library](#using-the-requests-library)
    - [Making an HTTP GET Request](#making-an-http-get-request)
    - [Making HTTP POST/PUT Requests](#making-http-postput-requests)
4. [Fetching JSON Resources](#fetching-json-resources)
5. [Manipulating Data from an External Service](#manipulating-data-from-an-external-service)

### 1. Fetching Internet Resources with urllib
The `urllib` library is part of Python's standard library and provides modules for working with URLs. It's suitable for basic HTTP requests.

```python
import urllib.request

url = "https://example.com"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
```

### 2. Decoding urllib Body Response
After making a request with `urllib`, you need to decode the response body, usually as UTF-8 or another appropriate encoding, to work with the content properly.

```python
response = urllib.request.urlopen(url)
decoded_response = response.read().decode('utf-8')
```

### 3. Using the requests Library
The `requests` library is a popular choice for making HTTP requests in Python. It offers a more user-friendly interface compared to `urllib`.

#### Making an HTTP GET Request
```python
import requests

url = "https://example.com"
response = requests.get(url)
if response.status_code == 200:
    content = response.text
    print(content)
```

#### Making HTTP POST/PUT Requests
```python
import requests

url = "https://example.com"
data = {"key": "value"}

# POST Request
response = requests.post(url, data=data)

# PUT Request
response = requests.put(url, data=data)
```

### 4. Fetching JSON Resources
To fetch JSON resources, you can use the `json()` method provided by the `requests` library to parse the JSON response.

```python
import requests

url = "https://api.example.com/data.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
```

### 5. Manipulating Data from an External Service
Once you've fetched data from an external service, you can manipulate it as needed. For example, if you've retrieved JSON data, you can access and modify it as a Python dictionary.

```python
import requests

url = "https://api.example.com/data.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Accessing data
    value = data["key"]

    # Modifying data
    data["new_key"] = "new_value"

    # Iterating through data
    for item in data:
        print(item, data[item])
```

Remember to handle exceptions, such as network errors or invalid JSON, to ensure your code is robust in a real-world application.

These are the fundamental concepts for fetching and manipulating internet resources in Python. Depending on your specific needs, you may also want to explore more advanced features of these libraries and consider error handling, authentication, and performance optimizations.
