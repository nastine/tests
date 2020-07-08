import unittest
import secretary
from unittest.mock import patch
from unittest.mock import Mock

class SecretaryTest(unittest.TestCase):
    def setUp(self):
        with patch('secretary.input', lambda *args: 'q'):
            secretary.main()
            self.dirs, self.docs = secretary.directories, secretary.documents
            

    def test_people(self):
        self.assertEqual(secretary.people('10006'), 'Аристарх Павлов')
        self.assertNotEqual(secretary.people('11-2'), 'Аристарх Павлов')

    def test_delete(self):
        secretary.delete('11-2')
        self.assertNotIn('11-2', self.dirs['1'])
    

    def test_add(self):
        m = Mock()
        m.side_effect = ['passport', 'Ivan Ivanov', '3']
        with patch('builtins.input', lambda *args: m()):
            secretary.add('12345')
            self.assertIn('12345', self.dirs['3'])
        
    @patch('builtins.input', lambda *args: '3')
    def test_move(self):
        secretary.move('10006')
        self.assertIn('10006', self.dirs['3'])


    def test_add_shelf(self):
        secretary.add_shelf('5')
        self.assertIn('5', self.dirs.keys())

if __name__ == "__main__":
    unittest.main()