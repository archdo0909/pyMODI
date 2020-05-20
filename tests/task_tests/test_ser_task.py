import unittest
from unittest import mock

from modi.task.ser_task import SerTask


class TestSerTask(unittest.TestCase):
    """Tests for 'SerTask' class"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.mock_kwargs = {"ser_recv_q": None, "ser_send_q": None}
        self.serTask = SerTask(**self.mock_kwargs)
        self.serTask._list_modi_ports = mock.Mock(side_effect=lambda: [None])

    def tearDown(self):
        """Tear down test fixtures, if any."""
        del self.serTask

    # def test_open_conn(self):
    #     """Test open_conn method"""
    #     self.serTask.open_conn()


if __name__ == "__main__":
    unittest.main()
