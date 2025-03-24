# PartB.py
import unittest
from PartA import Staff, Manager

class TestStaffManager(unittest.TestCase):
    def setUp(self):
        self.staff = Staff("Sam", "1992-05-27", "M", 101, "34 Woodview Ashford")
        self.manager = Manager("Anh", "1988-09-23", "M", 202, "18b main street StoneyBatter", 10)

    def test_instance(self):
        self.assertIsInstance(self.staff, Staff)
        self.assertIsInstance(self.manager, Manager)
        self.assertIsInstance(self.manager, Staff)

    def test_not_instance(self):
        self.assertNotIsInstance(self.staff, Manager)
        self.assertNotIsInstance(123, Staff)

    def test_identity(self):
        alias = self.staff
        self.assertIs(self.staff, alias)
        self.assertIsNot(self.staff, Staff("Sam", "1992-05-27", "M", 101, "34 Woodview Ashford"))

    def test_update(self):
        # Staff updates
        self.staff.update_name("Samuel O'Connor")
        self.assertEqual(self.staff.name, "Samuel O'Connor")
        self.staff.update_name(123)  # should remain unchanged (invlid)
        self.assertEqual(self.staff.name, "Samuel O'Connor")
        
        self.staff.update_dob("1992-05-17")
        self.assertEqual(self.staff.dob, "1992-05-17")
        self.staff.update_dob(12345)
        self.assertEqual(self.staff.dob, "1992-05-17")
        
        self.staff.update_sex("Male")
        self.assertEqual(self.staff.sex, "Male")
        self.staff.update_sex(True)
        self.assertEqual(self.staff.sex, "Male")
        
        self.staff.update_staffID(102)
        self.assertEqual(self.staff.staffID, 102)
        self.staff.update_staffID(102.5)
        self.assertEqual(self.staff.staffID, 102)
        
        self.staff.update_address("Pavillion House Swords")
        self.assertEqual(self.staff.address, "Pavillion House Swords")
        self.staff.update_address(456)
        self.assertEqual(self.staff.address, "Pavillion House Swords")
        
        # Manager updates
        self.manager.update_years_of_experience(12)
        self.assertEqual(self.manager.years_of_experience, 12)
        self.manager.update_years_of_experience("Twelve")
        self.assertEqual(self.manager.years_of_experience, 12)

if __name__ == '__main__':
    unittest.main()
