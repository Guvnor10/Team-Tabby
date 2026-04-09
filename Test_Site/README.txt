Sprint 4 Project Setup and Usage Guide

Matomo Login Credentials
  Username: matomo
  Password: matomo_pass


Instructions

*Run all code in Visual Studio Code terminal*
1. Open in visual studio code and run docker compose up -d in the terminal.
2. Start the traffic generator by running the code: docker exec test_site-traffic-bot-1 touch /bot/start_bot
3. Stop the traffic generator by running the code: docker exec test_site-traffic-bot-1 rm /bot/start_bot
4. To run the unit tests for the traffic generator run the code: python -m unittest discover -s tests -p "*.py"
5. Run docker compose down
