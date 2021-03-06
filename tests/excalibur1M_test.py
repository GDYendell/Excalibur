import unittest

from pkg_resources import require
require("mock")
from mock import patch, MagicMock, ANY

from excaliburcalibrationdawn import Excalibur1M

Detector_patch_path = "excaliburcalibrationdawn.excaliburdetector" \
                      ".ExcaliburDetector"


class InitTest(unittest.TestCase):

    @patch('logging.getLogger')
    @patch(Detector_patch_path + '.__init__')
    def test_super_called(self, excalibur_detector_mock, get_mock):
        detector = MagicMock(name="test-detector", nodes=[1, 2], master_node=1,
                             servers=["test-server"],
                             ip_addresses=["192.168.0.1"])
        config = MagicMock(detector=detector)
        e = Excalibur1M(config)

        get_mock.assert_called_once_with("Excalibur1M")
        self.assertEqual(get_mock.return_value, e.logger)
        excalibur_detector_mock.assert_called_once_with(config)

    def test_given_too_few_nodes_then_error(self):
        detector = MagicMock(name="test-detector", nodes=[1], master_node=1,
                             servers=["test-server"],
                             ip_addresses=["192.168.0.1"])
        config = MagicMock(detector=detector)

        with self.assertRaises(ValueError):
            Excalibur1M(config)

    def test_given_too_many_nodes_then_error(self):
        detector = MagicMock(name="test-detector", nodes=[1, 2, 3],
                             master_node=1, servers=["test-server"],
                             ip_addresses=["192.168.0.1"])
        config = MagicMock(detector=detector)

        with self.assertRaises(ValueError):
            Excalibur1M(config)
