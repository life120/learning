# How does the internet actually work?

The internet is essentially a long piece of wire that connects all computers together. The computers can be classified as either a server or a client. A server is a machine that is always turned on 24/7 to "serve" its content when a request is made. A computer that is used by users to retrieve data from servers are called client. The long piece of wire is called the Internet Backbone. It is a large network of high speed transmission cables that extend to all parts of the world, connecting all computers together. Our connection to the internet is maintained by our Internet Service Provider (ISP e.g. Singtel)

So how does it work?

When you submit a URL through the browser (e.g. www.google.com), the browser will send the information to the ISP. The ISP will then send this URL to a Domain Name System (DNS) server where it will use the URL to find the corresponding IP. The IP is a address of a computer in the Internet Backbone. The IP address is then sent back to the client, who will then make another request to ISP with the host IP address and client's IP address. The request will be sent through the ISP, into the Internet Backbone, where it will then reach the server of the host IP address. The host will then reply with information from the request and send it back to the client's IP address via the Internet Backbone once more. 

All this happens in a matter of milliseconds.