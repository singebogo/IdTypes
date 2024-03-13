import threading

class StoppableThread(threading.Thread):

    def __init__(self,  group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super(StoppableThread, self).__init__(group=group, target=target, name=name,  args=args, kwargs=kwargs, daemon=daemon)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()