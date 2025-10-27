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
