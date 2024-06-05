import unittest
import interview_hard
import dns_hard
import length_medium
import drunk_medium
import discount_easy
import stuttering_easy
import sum_very_easy
import nextnum_very_easy

class TestInterview(unittest.TestCase):
    def test_less_than_6(self):
        self.assertEqual(interview_hard.interview([5,5,10,10,15,15,20], 100), "disqualified") 
    def test_first_two(self):
        self.assertEqual(interview_hard.interview([6,5,10,10,15,15,20,20], 100), "disqualified")
    def test_third_and_fourth(self):
        self.assertEqual(interview_hard.interview([5,5,15,10,15,15,20,20], 100), "disqualified")
    def test_fifth_and_sixth(self):
        self.assertEqual(interview_hard.interview([5,5,10,10,16,15,20,20], 100), "disqualified")
    def test_seventh_and_eigth(self):
        self.assertEqual(interview_hard.interview([5,5,10,10,15,15,21,20], 100), "disqualified")
    def test_total_time_greater(self):
        self.assertEqual(interview_hard.interview([5,5,10,10,15,15,20,20], 121), "disqualified")
    def test_qualified(self):
          self.assertEqual(interview_hard.interview([5,5,10,10,15,15,20,20], 120), "qualified")

class TestDNS(unittest.TestCase):
    def test_success(self):
        ip_address = '8.8.8.8'
        expected_domain = 'dns.google'
        result = dns_hard.get_domain(ip_address)
        self.assertEqual(result, expected_domain)
class TestLength(unittest.TestCase):
    def test_the_length(self):
        self.assertEqual(length_medium.number_length(560309403), 9)
class TestDrunk(unittest.TestCase):
    def test_int_to_string(self):
        self.assertEqual(drunk_medium.int_to_str(5), "5")
    def test_string_to_int(self):
        self.assertEqual(drunk_medium.str_to_int("10"), 10)
class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(discount_easy.dis(500, 50), 250)
class TestStuttering(unittest.TestCase):
    def test_stuttering(self):
        self.assertEqual(stuttering_easy.stutter("interesting"), "in... in... interesting?")
class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_very_easy.addition(2, 3), 5)
class TestNextNum(unittest.TestCase):
    def test_next(self):
        self.assertEqual(nextnum_very_easy.addition(15), 16)
