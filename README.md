## Project Overview
F1-Management System is a python based system to manage formula 1 entities such as Teams, Drivers, Races and the Race results.

The project models the relationships between:
- Teams: Each team can have multiple drivers
- Drivers: Each driver belongs to one team and can participate in many races
- Races: Each race has a winner and features multiple drivers
- Race Results: Tracks each driver's performance in a given race

## Project Author
This prject has been developed by Lisa Alusa

## Project Structure
F1-Project/
├── lib/
│   ├── models/
│   │   ├── team.py
│   │   ├── driver.py
│   │   └── race.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   ├── debug.py
│   └── __init__.py
├── tests/
│   ├── test_team.py
│   ├── test_driver.py
│   └── test_race.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
├── README.md
└── __init__.py

## Setup instructions: 
- Option 1: Using pipenv
# Install dependencies
pipenv install pytest sqlite3

# Activate virtual environment 
pipenv shell

# Install the package in development mode
pip install -e