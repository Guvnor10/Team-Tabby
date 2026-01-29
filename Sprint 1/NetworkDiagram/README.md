# Team Tabby Network Diagram Notes

This is my attempt at explaining the network diagram for Team Tabby’s Docker project.

I am still learning how this works, so the IP addresses and ports here are starting guesses and not locked in forever. 

Team Tabby Host:

This is the computer or VM that actually runs Docker.

Users hit the project through:

localhost:8000  
localhost:8080  

I picked those because they are common for development and it let me separate the main site from analytics.

Docker Bridge Network:

This big box is Docker’s private network.

Subnet: 172.22.0.0/18  

From what I understand, Docker gives containers private IPs like this so they can talk to each other without being exposed directly.

tabby-web main site:

This container runs the actual website.

DNS: web  
IP: 172.22.0.10  
Port: 80  

The DNS name is just how the other containers would find it. Port 80 made sense to me since it is the normal HTTP port.

tabby-analytics:

This handles click tracking and analytics.

DNS: analytics  
IP: 172.22.0.20  
Port: 8080  

It runs separately from the main site and talks over HTTP inside Docker.

tabby-web-db:

This is the website’s database.

IP: 172.22.0.11  
Port: 3306  

I used 3306 because that is the default I usually see for databases (or what i saw when i was doing a sql section in a class).

tabby-analytics-db:

This stores analytics data.

IP: 172.22.0.21  
Port: 3306  

Keeping this separate just felt cleaner and easier to grow later.

tabby-traffic:

This can a little Python script that fakes site visits if needed(got the idea from a different class).

IP: 172.22.0.30  

It is mainly for testing and is not meant to be accessed from the host.

Arrows in the Diagram:

Host to tabby-web  
8000 to 80  

That shows port forwarding into the container.

tabby-web to tabby-analytics  
HTTP  

Those two talk to each other inside Docker.

tabby-web to tabby-web-db  
3306  

Database connection.

tabby-analytics to tabby-analytics-db  
3306  

Analytics database connection.

tabby-traffic to tabby-web  

Fake traffic being sent in.

Why I picked these values:

The IP range is private and looks similar to what Docker usually hands out.

The ports are common web and database ports.

The DNS names match the service names so containers can find each other.

I split the databases just to keep site data and analytics data separate.

What this diagram is for:

This is an early draft of how Team Tabby’s system could be wired together.

It is mostly about showing traffic flow, which parts are public, and which ones stay inside Docker.
