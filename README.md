# Team Tabby Sprint 3 - Mealie with Ackee Analytics

This project is my Sprint 3 Docker Compose setup for adding web analytics to our target website. For this version, I used Mealie as the target website and Ackee as the analytics package.

The goal of this setup is to make it where someone can run the stack with Docker Compose, open the Mealie site, open the Ackee dashboard, click around the site, and see the analytics update.

 What is in this project

This stack includes:

- Mealie
- PostgreSQL
- Ackee
- MongoDB
- Nginx reverse proxy

Mealie is the website being tracked.  
PostgreSQL is the database for Mealie.  
Ackee is the analytics dashboard.  
MongoDB is the database for Ackee.  
Nginx is used as a reverse proxy so I can inject the Ackee tracking script into Mealie without having to edit Mealie source code directly.

 Main links

Once the stack is running, these are the main URLs:

- Mealie: `http://localhost:8080`
- Ackee: `http://localhost:3000`

 How it works

The tracking works through Nginx.

When someone opens Mealie through `http://localhost:8080`, the request first goes through the Nginx proxy. Nginx forwards the request to the Mealie container and injects the Ackee tracking script into the HTML before the page is sent back to the browser.

That way, page visits on Mealie get sent over to Ackee and can be seen on the dashboard.

 Why I used bind mounts

I switched this project over to bind mounts so the working data is stored in project folders instead of only inside Docker volumes.

That matters for this setup because Ackee uses a domain ID for tracking, and that domain information is stored in the Ackee database. If that data gets wiped or is only living in Docker volumes on one machine, then somebody else pulling the project could run into problems where tracking no longer works.

Using bind mounts makes the setup a lot more portable for teammates and for grading.

 Important files and folders

- `compose.yml`  
  This is the main Docker Compose file for the project.

- `nginx/default.conf`  
  This is the Nginx config that forwards traffic to Mealie and injects the Ackee tracking script.

- `ackee-data/`  
  This stores the MongoDB data for Ackee.

- `mealie-data/`  
  This stores the Mealie app data.

- `mealie-db/`  
  This stores the PostgreSQL data for Mealie.

 How to run it

From the project folder, run:

```powershell
docker compose up -d

 How to test it

1. Open Mealie at `http://localhost:8080`
2. Open Ackee at `http://localhost:3000`
3. Refresh Mealie a few times and click around the site
4. Look at the Ackee dashboard and make sure the numbers update


Important testing note

Depending on browser cookies or saved session data, Ackee may ignore visits from the same normal browser session. If that happens, the easiest fix is to test Mealie in a private browser window.

The best way to test it is:

- keep Ackee open in your normal browser window at `http://localhost:3000`

- open Mealie in an InPrivate or Incognito window at `http://localhost:8080`

It helps if you have both pages side by side

- refresh and click around in Mealie there (there is also a live portion)
- then go back to the Ackee dashboard and check the stats

This helps avoid old cookies or browser state causing visits to be ignored.

 How to confirm the tracker is in the page
curl.exe http://localhost:8080 | findstr pixel.js