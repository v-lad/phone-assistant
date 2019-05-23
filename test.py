import pytest
import assistant
from random import randint


class TestPhoneAssistant:

    def test_negative_number_enter(self):
        """
        Negative numbers have not be entered
        """

        assistant.input = lambda arg: '-124'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'It can`t be negative'

    def test_not_a_number_enter(self):
        """
        Letters or symbols that not digits have not be entered
        """

        assistant.input = lambda arg: 'bad number'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'Invalid data'

    def test_infinity_enter(self):
        """
        If entered 'inf', assistant blocks it reversed word for infinity
        and it have to be handled
        """

        assistant.input = lambda arg: 'inf'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'Nice try'

    def test_minus_infinity_enter(self):
        """
        If entered '-inf', assistant blocks it reversed word for minus
        infinity and it have to be handled
        """

        assistant.input = lambda arg: '-inf'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'Nice try'

    def test_three_digits_enter(self):
        """
        All numbers from db ([380675674432, 380672832500, 380983567721])
        are returned with '380' template
        """

        assistant.input = lambda arg: '380'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == [380675674432, 380672832500, 380983567721]

    def test_five_digits_enter(self):
        """
        Two numbers from db ([380675674432, 380672832500, 380983567721])
        are returned with '38067' template
        """

        assistant.input = lambda arg: '38067'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == [380675674432, 380672832500]

    def test_six_digits_enter(self):
        """
        One numbers from db ([380675674432, 380672832500, 380983567721])
        are returned with '380983' template
        """

        assistant.input = lambda arg: '380983'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == [380983567721]

    def test_no_coincidence_enter(self):
        """
        No numbers from db ([380675674432, 380672832500, 380983567721])
        are returned with '1' template
        """

        assistant.input = lambda arg: '1'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == []

    def test_no_input(self):
        """
        There must be at least one digit
        """

        assistant.input = lambda arg: ''
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'Invalid data'

    def test_input_with_sign(self):
        """
        Input have to be without any signs
        """

        assistant.input = lambda arg: '+38093'
        db = [380675674432, 380672832500, 380983567721]
        result = assistant.find_numbers(db)
        assert result == 'Enter number without signs'

    def test_gt_ten_coincidence(self):
        """
        Only ten numbers from random db with country code '380'
        are returned with '380' template
        """

        assistant.input = lambda arg: '380'
        db = assistant.generate_random_numbers(100, '380')
        result = assistant.find_numbers(db)
        assert result == [num for num in db if str(num).startswith(assistant.input(None))][:10]
        assert len(result) == 10

    def test_four_digits_random_db(self):
        """
        Maximum ten numbers from random db can be returned with 
        '380' template
        """

        assistant.input = lambda arg: '3809'
        db = assistant.generate_random_numbers(100)
        result = assistant.find_numbers(db)
        assert len(result) <= 10