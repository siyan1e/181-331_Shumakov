import unittest
import main

test_data = [
    {
        # Позитивный сценарий

        'input_string': 'съешь ещё этих мягких французских булок, да выпей чаю',
        'shift': 3,
        'output_string': 'фэиыятудоиьитудоахлштудопвжнлштудочугрщцкфнлштудодцоснктхтудозгтудоеютимтудоъгб'
    },
    {
        # Негативный сценарий

        'input_string': 'съешь ещё этих мягких французских булок, да выпей чаю',
        'shift': 3,
        'output_string': 'бйфзляарыфихяарымвшеяарыьотъшеяарыдапэёгчбъшеяарыргыюъчявяарыупяарыскяфщяарыжпн'
    }
]


class TestMain(unittest.TestCase):

    def test(self):
        for data in test_data:
            output_string = main.encrypt(data['input_string'], data['shift'])
            self.assertEqual(output_string, data['output_string'])


if __name__ == '__main__':
    unittest.main()
