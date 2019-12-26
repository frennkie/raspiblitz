import os
import glob
import unittest

from blitztui import config

path_tests = os.path.dirname(__file__)
path_data = os.path.join(path_tests, 'data')


class TestLndConfig(unittest.TestCase):
    """ blitztui.config.LndConfig """
    def test_init(self):
        obj = config.LndConfig()
        self.assertIsInstance(obj, config.LndConfig)
        self.assertEqual(obj.abs_path, "/mnt/hdd/lnd/lnd.conf")

    def test_parser_multi(self):

        for file_path in glob.glob(os.path.join(path_data, "lnd*.conf*")):
            print("\n .. running on: {} .. ".format(file_path), end="")

            obj = config.LndConfig(file_path)
            self.assertIsInstance(obj, config.LndConfig)
            self.assertEqual(obj.abs_path, file_path)

            obj.reload()

            self.assertIsInstance(obj.rpc_listen, str)
            self.assertIsInstance(obj.rpc_listen_host, str)
            self.assertIsInstance(obj.rpc_listen_port, int)


class TestRaspiBlitzConfig(unittest.TestCase):
    """ blitztui.config.RaspiBlitzConfig """
    def test_init(self):
        obj = config.RaspiBlitzConfig()
        self.assertIsInstance(obj, config.RaspiBlitzConfig)
        self.assertEqual(obj.abs_path, "/mnt/hdd/raspiblitz.conf")

    def test_parser_multi(self):

        for file_path in glob.glob(os.path.join(path_data, "raspiblitz*.conf*")):
            print("\n .. running on: {} .. ".format(file_path), end="")

            obj = config.RaspiBlitzConfig(file_path)
            self.assertIsInstance(obj, config.RaspiBlitzConfig)
            self.assertEqual(obj.abs_path, file_path)

            obj.reload()

            self.assertIsInstance(obj.auto_nat_discovery, bool)
            self.assertIsInstance(obj.auto_pilot, bool)
            self.assertIsInstance(obj.auto_unlock, bool)


class TestRaspiBlitzInfo(unittest.TestCase):
    """ blitztui.config.RaspiBlitzInfo """
    def test_init(self):
        obj = config.RaspiBlitzInfo()
        self.assertIsInstance(obj, config.RaspiBlitzInfo)
        self.assertEqual(obj.abs_path, "/home/admin/raspiblitz.info")

    def test_parser_multi(self):

        for file_path in glob.glob(os.path.join(path_data, "raspiblitz*.info*")):
            print("\n .. running on: {} .. ".format(file_path), end="")

            obj = config.RaspiBlitzInfo(file_path)
            self.assertIsInstance(obj, config.RaspiBlitzInfo)
            self.assertEqual(obj.abs_path, file_path)

            obj.reload()

            self.assertIsInstance(obj.base_image, str)
            self.assertIsInstance(obj.chain, str)



if __name__ == '__main__':
    unittest.main()
