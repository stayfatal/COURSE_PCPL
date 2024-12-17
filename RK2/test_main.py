import unittest
from main_refactored import Computer, DisplayClass, ComputerAndDisplayClass,list_computers_with_name_ending_ov, list_average_threads_per_display, list_display_classes_starting_with_n

class TestMain(unittest.TestCase):

    def setUp(self):
        self.display_classes = [
            DisplayClass(id=1, name="Quantum"),
            DisplayClass(id=2, name="Cyber"),
            DisplayClass(id=3, name="Nano"),
            DisplayClass(id=4, name="Titan"),
            DisplayClass(id=5, name="Nexus")
        ]

        self.computers = [
            Computer(id=1, name="Alpha", cost=50000),
            Computer(id=2, name="Beta", cost=20000),
            Computer(id=3, name="Gamma", cost=70000),
            Computer(id=4, name="Delta", cost=90000),
            Computer(id=5, name="Epsilon", cost=30000)
        ]

        self.links = [
            ComputerAndDisplayClass(display_class_id=1, computer_id=1),
            ComputerAndDisplayClass(display_class_id=1, computer_id=3),
            ComputerAndDisplayClass(display_class_id=2, computer_id=2),
            ComputerAndDisplayClass(display_class_id=3, computer_id=3),
            ComputerAndDisplayClass(display_class_id=4, computer_id=4),
            ComputerAndDisplayClass(display_class_id=5, computer_id=1),
            ComputerAndDisplayClass(display_class_id=5, computer_id=5),
            ComputerAndDisplayClass(display_class_id=2, computer_id=4)
        ]

    def test_list_computers_with_name_ending_ov(self):
        result = list_computers_with_name_ending_ov(self.computers, self.display_classes, self.links)
        expected = [('Epsilon', 'Nexus')]
        self.assertEqual(result, expected)

    def test_list_average_threads_per_display(self):
        result = list_average_threads_per_display(self.display_classes, self.computers, self.links)
        expected = [('Nexus', 40000.0), ('Cyber', 55000.0), ('Quantum', 60000.0), ('Nano', 70000.0), ('Titan', 90000.0)]
        self.assertEqual(result, expected)

    def test_list_display_classes_starting_with_n(self):
        result = list_display_classes_starting_with_n(self.display_classes, self.computers, self.links)
        expected = [
            ('Nano', ['Gamma']),
            ('Nexus', ['Alpha', 'Epsilon'])
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()