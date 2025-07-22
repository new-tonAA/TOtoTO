import threading

class ThreadLocalUtil:
    # Provide ThreadLocal object
    _thread_local = threading.local()

    @staticmethod
    def get():
        """Get the value for the current thread"""
        return getattr(ThreadLocalUtil._thread_local, 'value', None)

    @staticmethod
    def set(value):
        """Set the value for the current thread"""
        ThreadLocalUtil._thread_local.value = value

    @staticmethod
    def remove():
        """Remove the value for the current thread to prevent memory leaks"""
        if hasattr(ThreadLocalUtil._thread_local, 'value'):
            del ThreadLocalUtil._thread_local.value