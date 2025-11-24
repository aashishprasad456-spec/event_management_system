# event_management_system

Project Title:
Event Management Project

# Overview
A desktop application built with Python and Tkinter for managing campus events, volunteers, and participants. The system provides a user-friendly interface to create events, register volunteers, and manage participant registrations.

# Features

# Event Management
- Create new events with details like name, category, date, time, location, and maximum capacity
- View all created events in a organized table
- Automatic event ID generation
- Input validation for required fields

# Volunteer Registration
- Register volunteers for specific events
- Prevent duplicate registrations using email validation
- Track registration timestamps
- View all registered volunteers

# Participant Management
- Register participants for events
- Capacity management to prevent overbooking
- Duplicate email checking
- Phone number collection
- Real-time registration tracking

# File Structure

The application uses three text files for data storage:

- `events.txt` - Stores event information
- `vols.txt` - Stores volunteer registrations  
- `parts.txt` - Stores participant registrations

# Installation & Requirements

# Prerequisites
- Python 3.x
- Tkinter (usually comes with Python)
- No additional packages required

# Running the Application
1. Save the code as `event_manager.py`
2. Run the script:
   ```bash
   python event_manager.py
   ```

# How to Use

# Creating Events
1. Navigate to the "Events" tab
2. Fill in event details:
   - Event Name (required)
   - Category
   - Date
   - Start Time
   - End Time
   - Location
   - Maximum Participants
3. Click "Create Event"

# Registering Volunteers
1. Go to the "Volunteers" tab
2. Enter:
   - Event ID (from existing events)
   - Full Name
   - Email Address
3. Click "Register"

# Registering Participants
1. Open the "Participants" tab
2. Provide:
   - Event ID
   - Full Name
   - Email Address
   - Phone Number
3. Click "Register Participant"

# Data Format

# Events File Format
```
event_id|event_name|category|date|start_time|end_time|location|max_participants
```

# Volunteers File Format
```
volunteer_id|event_id|name|email|timestamp
```

# Participants File Format
```
participant_id|event_id|name|email|phone|timestamp
```

# Error Handling

- Prevents duplicate email registrations per event
- Validates event existence before registration
- Enforces maximum participant limits
- Requires all mandatory fields
- Provides user-friendly error messages

# Technical Details

- **GUI Framework**: Tkinter with ttk widgets
- **Data Storage**: Text files with pipe-separated values
- **ID Generation**: Random 6-character alphanumeric strings
- **Timestamp Format**: ISO format for accurate time tracking

# Limitations

- Data persists in text files (no database)
- No user authentication system
- Basic error handling
- No data export features

# Future Enhancements

- Database integration
- User authentication
- Email notifications
- Reporting and analytics
- Data export capabilities
- Event cancellation features

# Support

For issues or questions, check the input validation messages and ensure all required fields are properly filled. The system provides descriptive error messages to guide users through the registration process.

---
*Note: This is a standalone desktop application designed for single-computer use with local file storage.*
