# Quentin Docker Compose Lab

This project is a Docker Compose setup that runs two containers:

1. the Flask container runs the web site  
2. the Redis container keeps track of how many times the site is opened  

If you refresh the page the visit number goes up and the number is stored in Redis.

What You Will See When It Runs

When everything is working and you open the site in a browser, you should see:

a welcome message, a welcome png, and a visit counter that increases when you refresh.

If you only see an error page, that means something didn’t start correctly.

Tutorials Used

These are the videos that I looked at when learning Docker Compose basics:

1. TechWorld with Nana – https://www.youtube.com/watch?v=SXwC9fSwct8  
2. Programming with Mosh – https://www.youtube.com/watch?v=HG6yIjZapSA  
3. Jake Wright – https://www.youtube.com/watch?v=Qw9zlE3t8Ko  

How the Three Videos Influenced This Project

TechWorld with Nana helped me understand what Docker Compose is for and how multiple services can run together.

Programming with Mosh showed me the structure of the compose file, how to build images, map ports, and start everything with docker compose up.

Jake Wright’s video made the overall idea click and helped reinforce why one YAML file can control multiple containers.

All three contributed to this final setup with a Flask web service, a Redis service, and a working compose.yml file.

Things You Need Installed First

1. Docker Desktop  
Open it and wait until it says Engine running.

2. VS Code or another editor  
Used to view and edit the files. After setup it is optional.

How to Run This Project Step by Step

Step 1 Start Docker Desktop

Open Docker Desktop and make sure it is running.
You should see something green or the word running.

Leave Docker Desktop open in the background.

Step 2 Open a Terminal in the Project Folder

Open the folder quentin-docker-lab.

If you are using VS Code:

1. open the folder  
2. click Terminal at the top  
3. click New Terminal  

A terminal window should open at the bottom.

Step 3 Build and Start the Containers

In the terminal run:

docker compose up --build

This builds the web container, downloads Redis, and starts everything.

Step 4 Open the Site

Open a browser and go to:

http://localhost:8000

Refresh the page a few times and watch the number go up.

Step 5 Stop Everything

Go back to the terminal window.

Press CTRL and C together.

Then run:

docker compose down


What Each File Does:

compose.yml  
This controls the whole setup and tells Docker which containers to run.

Dockerfile  
This explains how the Flask container is built.

server.py  
This is the web app code that talks to Redis and shows the page.

requirements.txt  
This lists the Python libraries that get installed inside the container.

static folder  
This holds the image used on the site.

Troubleshooting

If something does not work:

make sure Docker Desktop is running  
make sure you ran the command inside the quentin-docker-lab folder  
make sure the browser is using port 8000  

If needed rebuild everything:

docker compose down  
docker compose up --build  
