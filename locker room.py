class Locker:  
    def __init__(self, locker_number, status="Available"):  
        self.locker_number = locker_number  
        self.status = status  
        self.user = None  
  
class LockerRoom:  
    def __init__(self):  
        self.lockers = {}  
  
    def add_locker(self, locker_number):  
        self.lockers[locker_number] = Locker(locker_number)  
  
  
  
 
  
    def remove_locker(self, locker_number):  
        if locker_number in self.lockers:  
            del self.lockers[locker_number]  
        else:  
            print("Locker not found.")  
  
    def rent_locker(self, locker_number, user):  
        if locker_number in self.lockers and self.lockers[locker_number].status == "Available":  
            self.lockers[locker_number].status = "Occupied"  
            self.lockers[locker_number].user = user  
            print(f"Locker {locker_number} rented to {user}.")  
        else:  
            print("Locker not available.")  
  
    def return_locker(self, locker_number):  
        if locker_number in self.lockers and self.lockers[locker_number].status == "Occupied":  
            self.lockers[locker_number].status = "Available"  
            self.lockers[locker_number].user = None  
            print(f"Locker {locker_number} returned.")  
        else:  
            print("Locker not occupied.")  
  
    def display_lockers(self):  
        print("Locker Room Status:")  
        for locker_number, locker in self.lockers.items():  
            print(f"Locker {locker_number}: {locker.status} ({locker.user})")  
  
  
def main():  
    locker_room = LockerRoom()  
  
    while True:  
        print("\nLocker Room Management System")  
        print("1. Add Locker")  
        print("2. Remove Locker")  
        print("3. Rent Locker")  
        print("4. Return Locker")  
        print("5. Display Lockers")  
        print("6. Exit")  
  
        choice = input("Choose an option: ")  
  
        if choice == "1":  
            locker_number = input("Enter locker number: ")  
            locker_room.add_locker(locker_number)  
        elif choice == "2":  
            locker_number = input("Enter locker number: ")  
            locker_room.remove_locker(locker_number)  
        elif choice == "3":  
            locker_number = input("Enter locker number: ")  
            user = input("Enter user name: ")  
            locker_room.rent_locker(locker_number, user)  
        elif choice == "4":  
            locker_number = input("Enter locker number: ")  
            locker_room.return_locker(locker_number)  
        elif choice == "5":  
  
  
 
  
            locker_room.display_lockers()  
        elif choice == "6":  
            break  
        else:  
            print("Invalid option. Please choose again.")  
  
if __name__ == "__main__":  
    main()  