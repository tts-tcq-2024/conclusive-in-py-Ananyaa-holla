import unittest
from unittest.mock import patch
from typewise_alert import check_and_alert,infer_breach


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
      self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')

    @patch('typewise_alert.send_to_controller')
    def test_check_and_alert_controller(self, mock_send_to_controller):
        batteryChar = {'coolingType': 'PASSIVE_COOLING'}
        temperatureInC = 30
        check_and_alert('TO_CONTROLLER', batteryChar, temperatureInC)
        mock_send_to_controller.assert_called_once_with('NORMAL')

    @patch('typewise_alert.send_to_email')
    def test_check_and_alert_email(self, mock_send_to_email):
        batteryChar = {'coolingType': 'HI_ACTIVE_COOLING'}
        temperatureInC = 50
        check_and_alert('TO_EMAIL', batteryChar, temperatureInC)
        mock_send_to_email.assert_called_once_with('TOO_HIGH')

    @patch('typewise_alert.send_to_email')
    def test_check_and_alert_email_low(self, mock_send_to_email):
        batteryChar = {'coolingType': 'MED_ACTIVE_COOLING'}
        temperatureInC = -5
        check_and_alert('TO_EMAIL', batteryChar, temperatureInC)
        mock_send_to_email.assert_called_once_with('TOO_LOW')


if __name__ == '__main__':
  unittest.main()
