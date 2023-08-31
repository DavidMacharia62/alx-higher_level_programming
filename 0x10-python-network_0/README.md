# README: Understanding URLs, HTTP, and Making Requests

## What is a URL (Uniform Resource Locator)?

A Uniform Resource Locator, or URL, is a standardized address used to identify and locate resources on the internet. It serves as a reference to a specific resource's location and how to access it. A URL typically consists of several components, including the scheme, domain, path, query string, and fragment identifier.

## What is HTTP (Hypertext Transfer Protocol)?

HTTP, or Hypertext Transfer Protocol, is a set of rules and conventions that govern how data is transferred and presented on the World Wide Web. It is the foundation of data communication on the internet and defines how web browsers and web servers interact.

## How to Read a URL:

A URL can be broken down into several parts:

- **Scheme**: The scheme specifies how to access the resource (e.g., HTTP, HTTPS, FTP).
- **Domain**: The domain name identifies the web server's address.
- **Sub-domain**: An optional prefix to the domain that can further specify a particular section or service of a website.
- **Port**: An optional port number that specifies the communication port for the server.
- **Path**: The path indicates the specific location of a resource on the server.
- **Query String**: Contains additional parameters for the resource, often used in search queries.
- **Fragment Identifier**: Specifies a specific section or anchor within a page.

## The Scheme for an HTTP URL:

The scheme for an HTTP URL is typically "http://" for unencrypted connections or "https://" for encrypted connections using SSL/TLS.

## What is a Domain Name?

A domain name is a human-readable label that represents a specific IP address or a group of IP addresses. It's used to identify a particular web server on the internet, making it easier for users to access websites without needing to remember numerical IP addresses.

## What is a Sub-domain?

A sub-domain is a subset of a larger domain and can be used to organize and categorize websites or services. For example, "blog.example.com" is a sub-domain of "example.com."

## How to Define a Port Number in a URL:

A port number can be specified in a URL using a colon followed by the port number. For example, "http://example.com:8080" indicates that the web server is listening on port 8080.

## What is a Query String?

A query string is a part of a URL that contains key-value pairs used to send additional data to the server. It usually follows a question mark and can be used for various purposes like passing parameters to web applications.

## What is an HTTP Request?

An HTTP request is a message sent by a client (e.g., a web browser) to a server to request a specific resource (e.g., a web page). It contains information about the desired action and may include headers, a request method, a URL, and a message body.

## What is an HTTP Response?

An HTTP response is a message sent by a web server to a client in response to an HTTP request. It contains the requested resource, along with response headers, a status code, and an optional message body.

## What are HTTP Headers?

HTTP headers are metadata associated with an HTTP request or response. They provide additional information about the data being transferred, such as content type, caching instructions, and authentication details.

## What is the HTTP Message Body?

The HTTP message body is the part of an HTTP request or response that contains the actual data being transferred. For example, in an HTTP POST request, the message body often contains form data or a JSON payload.

## What is an HTTP Request Method?

An HTTP request method is a verb that specifies the desired action to be performed on a resource. Common methods include GET (retrieve data), POST (submit data), PUT (update data), DELETE (remove data), and more.

## What is an HTTP Response Status Code?

An HTTP response status code is a three-digit numeric code sent by the server to indicate the outcome of an HTTP request. Common status codes include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).

## What is an HTTP Cookie?

An HTTP cookie is a small piece of data sent by a web server to a user's web browser. The browser stores this data and sends it back with subsequent requests to the same server. Cookies are often used for user authentication, tracking, and session management.

## How to Make a Request with cURL:

[cURL](https://curl.se/) is a command-line tool for making HTTP requests. To make a GET request with cURL, you can use the following command:

```bash
curl [URL]
```

You can specify different request methods and include headers and data as needed.

## What Happens When You Type google.com in Your Browser (Application Level):

1. The browser initiates a DNS (Domain Name System) lookup to resolve "google.com" to an IP address.

2. Once the IP address is obtained, the browser establishes a TCP connection to the web server at that IP address on port 80 (HTTP) or 443 (HTTPS).

3. The browser sends an HTTP GET request to the server for the resource specified in the URL.

4. The web server processes the request, retrieves the requested web page, and generates an HTTP response.

5. The browser receives the response, including the HTML content, and begins rendering the web page for the user to view.

This README provides an overview of fundamental concepts related to URLs, HTTP, and making HTTP requests, along with a brief introduction to cURL and the process of typing a URL in a browser at the application level. Further details and practical implementations can be explored through additional resources and hands-on experience.
