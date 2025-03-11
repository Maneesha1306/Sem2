class HotelRoom: 
    def __init__(self,room_number,rate_per_night): 
        self.__room_number=room_number 
        self.__is_occupied=False 
        self.__rate_per_night=rate_per_night 
    def get_room_no(self): 
        if self.__room_number>0: 
            return self.__room_number 
        else: 
            raise ValueError ("Room number should be positive") 
    def set_room_no(self,room_number): 
        self.__room_number=room_number 
    def get_rate_per_night(self): 
        if self.__rate_per_night>=0: 
            return self.__rate_per_night 
        else: 
            raise ValueError ("Rate should be greater than zero") 
    def set_rate_per_night(self,rate_per_night): 
        self.__rate_per_night=rate_per_night 
    def check_in(self): 
        if self.__is_occupied: 
            raise Exception ("Room is occupied already") 
        self.__is_occupied=True 
    def check_out(self): 
        if not self.__is_occupied: 
            raise Exception ("Room is vacant") 
        self.__is_occupied=False 
    def display_details(self): 
        print(f"Room Number : {self.__room_number}") 
        room_status="Occupied" if self.__is_occupied else "Not Occupied" 
        print(f"Room Status : {room_status}") 
        print(f"Rate per night : {self.__rate_per_night}")
try: 
    room_no=int(input("Enter the room number : ")) 
    rate=float(input("Enter the rate per night : ")) 
    room=HotelRoom(room_no,rate) 
    room.get_room_no() 
    room.get_rate_per_night() 
except Exception as e: 
    print(e) 
except ValueError as v: 
    print(v) 
check=input("(check in/check out): ").strip().lower() 
if check=="check in": 
    print("Room is successfully checked in ") 
    room.check_in()
elif check=="chech out": 
    print("Room is successfully checked out ")
    room.check_out() 
room.display_details() 