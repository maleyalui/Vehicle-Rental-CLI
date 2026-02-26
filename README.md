# Vehicle-Rental-CLI
A simple command-line application for managing vehicle rentals.  
Users can register/login, browse and rent vehicles, return them, while admins can manage the vehicle inventory.

**Built as a group project** to demonstrate:
- Object-Oriented Programming (classes, inheritance, encapsulation)
- Modular Python structure (models, services, utils)
- File-based persistence using JSON
- User authentication with password hashing
- Role-based access control (customer vs admin)
- Clean interactive CLI menus

## Features

### Customer Features
- Register and login
- View available vehicles
- View currently rented vehicles
- Rent a vehicle for a specified number of days
- Return a rented vehicle
- View personal rental history

### Admin Features
- View all vehicles
- Add new vehicles
- Change vehicle status (available / rented / maintenance)
- View all rentals (with customer and vehicle details)

### Technical Highlights
- Passwords stored using SHA-256 hashing
- Separate JSON files for users, vehicles, and rentals
- No external dependencies (only built-in Python libraries)

## Tech Stack

- Python 3.x
- Built-in modules: `json`, `os`, `datetime`, `hashlib`
- No pip installs required

## Installation & Running

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd vehicle_rental_cli
   python3 main.py

## Project Structure
textvehicle_rental_cli/
├── main.py                     # Application entry point & menus
├── auth.py                     # Authentication helpers
├── decorators.py               # Role-based decorators
├── models/                     # Data models
│   ├── users.py
│   ├── vehicle.py
│   └── rental.py
├── services/                   # Business logic & JSON persistence
│   ├── users_services.py
│   ├── vehicle_services.py
│   └── rental_services.py
└── data/                       # Persistent storage
    ├── users.json
    ├── vehicles.json
    └── rentals.json

## Team Members & Contributions

Luie Maleya – Project coordination, main.py, login flow, integration, README
Priscillah Kamau – Rental services (rent/return logic), bug fixes
Mitchelle Wanjiku – Models (users.py, vehicle.py), partial services
Mulki Mohammed – Vehicle services, output formatting, documentation ,ReadMe