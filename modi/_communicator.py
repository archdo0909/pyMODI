
import threading as th
import multiprocessing as mp

from modi._communicator_task import CommunicatorTask
from modi._ser_task import SerTask
from modi._can_task import CanTask


class Communicator(mp.Process):

    def __init__(self, recv_q, send_q):
        super().__init__()
        task = CanTask if self.__is_modi_pi() else SerTask
        self.__task = task(recv_q, send_q)
        self.__delay = 0.001
        self.__stop = mp.Event()

    def __is_modi_pi(self):
        return CommunicatorTask.is_on_pi() and not CommunicatorTask.is_network_module_connected()

    def run(self):
        self.__task.open_conn()

        read_thread = th.Thread(
            target=self.__task.run_read_data, args=(self.__delay,)
        )
        read_thread.daemon = True
        read_thread.start()

        write_thread = th.Thread(
            target=self.__task.run_write_data, args=(self.__delay,)
        )
        write_thread.daemon = True
        write_thread.start()

        self.__stop.wait()

    def stop(self):
        """ Stop executor task
        """

        self.__stop.set()


    
