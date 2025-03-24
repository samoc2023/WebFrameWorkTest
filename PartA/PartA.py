class Staff:
    def __init__(self, name, dob, sex, staffID, address):
        if not isinstance(name, str): raise ValueError("name must be a string")
        if not isinstance(dob, str): raise ValueError("DoB must be a string")
        if not isinstance(sex, str): raise ValueError("sex must be a string")
        if not isinstance(staffID, (int, str)): raise ValueError("staffID must be an int or string")
        if not isinstance(address, str): raise ValueError("address must be a string")
        self.name = name
        self.dob = dob
        self.sex = sex
        self.staffID = staffID
        self.address = address

    def print_attributes(self):
        print(f"Name: {self.name}, DoB: {self.dob}, Sex: {self.sex}, StaffID: {self.staffID}, Address: {self.address}")

    def update_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Error: Name must be a string.")

    def update_dob(self, new_dob):
        if isinstance(new_dob, str):
            self.dob = new_dob
        else:
            print("Error: DoB must be a string.")

    def update_sex(self, new_sex):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Error: Sex must be a string.")

    def update_staffID(self, new_staffID):
        if isinstance(new_staffID, (int, str)):
            self.staffID = new_staffID
        else:
            print("Error: StaffID must be an int or string.")

    def update_address(self, new_address):
        if isinstance(new_address, str):
            self.address = new_address
        else:
            print("Error: Address must be a string.")


class Manager(Staff):
    def __init__(self, name, dob, sex, staffID, address, years_of_experience):
        super().__init__(name, dob, sex, staffID, address)
        if not isinstance(years_of_experience, int): raise ValueError("Years of experience must be an integer")
        self.years_of_experience = years_of_experience

    def print_all_attributes(self):
        self.print_attributes()
        print(f"Years of Experience: {self.years_of_experience}")

   

    def update_years_of_experience(self, new_years):
        if isinstance(new_years, int):
            self.years_of_experience = new_years
        else:
            print("Error: Years of experience must be an integer.")


if __name__ == "__main__":
    # Create instances
    staff1 = Staff("Sam", "1992-27-05", "M", 101, "34 Woodview Ashford")
    manager1 = Manager("Anh", "1988-09-23", "M", 202, "18b main street StoneyBatter", 10)

    # Print initial attributes
    print("=== Initial Staff ===")
    staff1.print_attributes()
    print("=== Initial Manager ===")
    manager1.print_all_attributes()

    # Update examples for Staff
    print("\n--- Updating Staff ---")
    staff1.update_name("Samuel O'Connor")
    staff1.update_name(123)
    staff1.update_dob("1992-05-17")
    staff1.update_dob(12345)
    staff1.update_sex("Male")
    staff1.update_sex(True)
    staff1.update_staffID(102)
    staff1.update_staffID(102.5)
    staff1.update_address("pavillionhouse Swords")
    staff1.update_address(18)
    print("=== Updated Staff ===")
    staff1.print_attributes()

    # Update examples for Manager
    print("\n--- Updating Manager ---")
    manager1.update_years_of_experience(12)
    manager1.update_years_of_experience("Twelve")
    print("=== Updated Manager ===")
    manager1.print_all_attributes()
