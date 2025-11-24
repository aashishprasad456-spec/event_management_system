Project Statement
# Problem Statement

Managing campus events manually often leads to issues such as disorganized event records, duplicate volunteer entries, difficulty tracking event capacity, and lack of a centralized platform for event organizers. Without a structured system, storing and retrieving event or volunteer data becomes inefficient and time-consuming.

The Campus Event Manager solves this problem by providing a simple GUI-based application that allows users to create events, register volunteers, and maintain all records in an organized and accessible manner.

# Scope of the Project

The scope of this project includes:

Creating a desktop-based application using Python and Tkinter.

Allowing event organizers to add and view campus events.

Enabling volunteers to register for specific events.

Automatically generating unique IDs for both events and volunteers.

Storing data persistently using .dat files.

Providing a clean and user-friendly tab-based interface.

Out of scope:

Online access or cloud storage

Multi-user authentication

Editing or deleting previously stored events/volunteers (can be added in future)

Database integration

# Target Users

This project is designed for:

College event organizers who need a simple system to handle event data.

Student volunteers who want to register quickly for events.

Clubs & committees that frequently run campus activities.

Small institutions looking for a lightweight event management tool.

# High-Level Features
1. Event Management

Add new events with details like date, time, type, and venue.

Auto-generate unique event IDs.

View all events in a structured table.

2. Volunteer Registration

Register volunteers with name and email.

Validate event ID before registration.

Prevent duplicate volunteer registrations for the same event.

3. Data Persistence

Stores all data in local .dat files.

Automatically creates required data files if not found.

4. User-Friendly Interface

Tab-based layout for easy navigation.

Clean UI using Tkinter widgets.

Scrollable tables for viewing large lists.