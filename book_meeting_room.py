from datetime import datetime

class Booking:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def isOverlap(self, booking_to_check):
        return not (self.end_time <= booking_to_check.start_time or booking_to_check.start_time<=self.start_time)

    def __str__(self):
        return f"{self.start_time} - {self.end_time} : {self.name}"

class MeetingRoom:
    def __init__(self, roomName):
        self.roomName = roomName
        self.bookings = []

    def book_room(self, name, start_time, end_time):
        new_booking = Booking(name, start_time, end_time)
        for booking in self.bookings:
            if booking.isOverlap(new_booking):
                return False
        self.bookings.append(new_booking)
        self.bookings.sort(key=lambda b:b.start_time)
        return True

    def cancel_room(self, name, start_time):
        for booking in self.bookings:
            if ((booking.name == name) and (booking.start_time == start_time)):
                self.bookings.remove(booking)
                return True
        return False

    def get_schedule(self):
        if not self.bookings:
            return "No Bookings Made for this room"

        return self.roomName+"Schedule:\n"+"\n".join(str(b) for b in self.bookings)

    def isAvailable(self, start_time, end_time):
        new_booking = Booking("Dummy", start_time, end_time)
        for booking in self.bookings:
            if booking.isOverlap(new_booking):
                return False
        return True


class BookingHelper:
    def __init__(self):
        self.rooms = {}

    def add_room(self, roomName):
        if roomName not in self.rooms:
            self.rooms[roomName] = MeetingRoom(roomName)

    def book_meeting_room(self, name, roomName, start_time, end_time):
        self.add_room(roomName)
        return self.rooms[roomName].book_room(name, start_time, end_time)

    def cancel_meeting(self, name, roomName, start_time):
        if roomName not in self.rooms:
            return False
        return self.rooms[roomName].cancel_room(name, start_time)

    def show_room_schedule(self, roomName):
        if roomName not in self.rooms:
            return "Room Not Present"
        return self.rooms[roomName].get_schedule()

    def check_room_availability(self, start_time, end_time):
        available_rooms = []
        for roomName, room in self.rooms.items():
            if room.isAvailable(start_time, end_time):
                available_rooms.append(room.roomName)
        return available_rooms

    
def parse_time(timeStr):
    return datetime.strptime(timeStr, "%H:%M")


def main():
    booking_helper = BookingHelper()
    commands = ["BOOK", "CANCEL", "CHECKAVAILABILITY", "SHOWSCHEDULE", "QUIT"]

    while True:
        input_cmd = input().strip().split()
        print(input_cmd)
        action = input_cmd[0]

        try:
            if action == "BOOK" and len(input_cmd)==5:
                name,roomName,start_time,end_time = input_cmd[1], input_cmd[2], parse_time(input_cmd[3]), parse_time(input_cmd[4])
                if booking_helper.book_meeting_room(name, roomName, start_time, end_time):
                    print("Room Booked")
            
            elif action == "CANCEL" and len(input_cmd)==4:
                name, roomName, start_time = input_cmd[1], input_cmd[2], parse_time(input_cmd[3])
                if booking_helper.cancel_meeting(name, roomName, start_time):
                    print("Meeting Cancelled")

            elif action == "SHOW_SCHEDULE" and len(input_cmd)==2:
                roomName = input_cmd[1]
                print(booking_helper.show_room_schedule(roomName))

            elif action == "CHECK_AVAILABILITY" and len(input_cmd)==3:
                start_time, end_time = parse_time(input_cmd[1]), parse_time(input_cmd[2])
                available = booking_helper.check_room_availability(start_time, end_time)
                print(f"Available Rooms from {start_time} to {end_time}:")
                for room in available:
                    print(room)
                
            elif action == "QUIT":
                print("QUITTING")
                break

            else:
                print("Enter Valid Action")

        except Exception as e:
            print(f"Error - {e}")

if __name__=="__main__":
    main()
