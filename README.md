# event_management_system

Project Title:
Event Management Project

Overview of the Project

The Campus Event Manager is a Python-based desktop application built using Tkinter. It allows users to manage campus events and register volunteers for those events. The system stores event and volunteer information in lightweight .dat files, making it simple and easy to use without requiring heavy databases.

The project follows a modular OOP-based structure with separate classes for handling events, volunteers, file operations, and UI components.

Features
Event Management

Add new campus events

Store event details (name, type, date, time, venue, max capacity)

Auto-generate unique event IDs

View all events in a table format

Volunteer Management

Register volunteers for specific events

Prevent duplicate registrations

Auto-generate volunteer IDs

View all volunteer details in a table

Other Features

Simple GUI using Tkinter

Separate tabs for Events and Volunteers

Data persistence using local .dat files

Clean modular structure using classes

Technologies / Tools Used

Python 3.x

Tkinter (GUI framework)

OS module (file handling)

Random module (unique ID generator)

Datetime module (timestamping)

Steps to Install & Run the Project

Download or clone the repository

git clone https://github.com/your-repo/event-manager.git

Navigate into the project folder

cd event-manager

Run the application

python main.py

Note: Make sure Python 3.x is installed on your system.

Instructions for Testing

Open the app using python main.py.

Go to Events tab:

Add an event by filling all fields.

Check if the event appears in the events list.

Go to Volunteers tab:

Register a volunteer using a valid Event ID.

Check whether the volunteer appears in the list.

Try registering the same email for the same event → It should show an error.

Close and reopen the application → All previous data should still be visible.

Screenshots (Optional)

You can add screenshots like:

Event creation window

Volunteers registration window

Final dashboard view
