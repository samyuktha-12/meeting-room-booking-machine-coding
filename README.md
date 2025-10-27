# meeting-room-booking-machine-coding

You are tasked with implementing a command-line system to manage meeting room reservations for a small office.
Functional Requirements
Book a Room
Cancel a Booking
Check Room Schedule
Check Availability

### Sample Input

```
BOOK Alice Room1 09:00 10:00
BOOK Bob Room1 10:00 11:00
BOOK Charlie Room2 09:30 10:30
BOOK Alice Room2 10:30 11:30
CANCEL Bob Room1 10:00
SHOW_SCHEDULE Room1
SHOW_SCHEDULE Room2
CHECK_AVAILABILITY 10:00 11:00
```

### Sample Output
```
Room1 Schedule:
09:00 - 10:00 : Alice
Room2 Schedule:
09:30 - 10:30 : Charlie
10:30 - 11:30 : Alice
Available Rooms from 10:00 to 11:00:
Room1
```

HH:MM -> 24 hr format for a single day

## Solution

#### Overview

The system manages room bookings, cancellations, schedules, and availability. It ensures no overlapping bookings and allows users to interact with rooms through various operations.

#### Key Components

1. ```Booking``` Class:

- Attributes: ```name```, ```start_time```, ```end_time```

- Methods:

  - ```isOverlap(booking_to_check)```: Checks if two bookings overlap.

2. ```MeetingRoom``` Class:

- Attributes: ```roomName```, ```bookings``` (list of Booking).

- Methods:

  - ```book_room(name, start_time, end_time)```: Books the room if available.

  - ```cancel_room(name, start_time)```: Cancels a booking.

  - ```get_schedule()```: Returns room's schedule.

  - ```isAvailable(start_time, end_time)```: Checks availability for the time range.

3. ```BookingHelper``` Class:

- Attributes: ```rooms``` (dict of room names → MeetingRoom objects).

- Methods:

  - ```book_meeting_room()```: Books a meeting room.

  - ```cancel_meeting()```: Cancels a booking.

  - ```show_room_schedule()```: Displays a room's booking schedule.

  - ```check_room_availability()```: Checks all rooms for availability.

4. Utility Function:

- ```parse_time(timeStr)```: Converts time string to datetime.

#### Design Pattern:

- ```Singleton```: A single instance of BookingHelper manages multiple rooms.

- ```Factory```: Rooms are dynamically created when booked for the first time.

- ```Composite```: MeetingRoom aggregates Booking instances for each room.

#### Operation Flow

1. Booking:

- Check availability (isAvailable()), if free, create a Booking and add to room's list (book_room()).

2. Cancellation:

- Search and remove the Booking from the room's list (cancel_room()).

3. Schedule:

- Return formatted list of bookings for a room (get_schedule()).

4. Availability:

- Check each room’s schedule (isAvailable()) for the specified time.

#### Key Constraints

- No overlap: Ensures rooms are not double-booked.

- Valid input: Time is in HH:MM format.

- Room availability: Rooms must be checked before booking.

