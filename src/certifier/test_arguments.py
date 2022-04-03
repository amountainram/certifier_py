import unittest
from certifier.arguments import get_parser


class TestArguments(unittest.TestCase):

    def test_setup_argument(self):
        parsed = get_parser().parse_args(['setup'])
        self.assertEqual(parsed.command, 'setup')


if __name__ == '__main__':
    unittest.main()
