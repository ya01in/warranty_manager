import time

class Counter:

    def __init__(self):
        pass

    def get_time(self) -> float:
        """Get current unix time

        Returns:
            float: unix format time second
        """
        return time.time()

    def unix2day(self, unix_time: float) -> int:
        """turn time unit from second to day

        Args:
            unix_time (float): unix format time in second

        Returns:
            int: day count
        """
        return int(unix_time // 86400.0)

    def is_due(self, due_time: float) -> bool:
        """check if warrenty time is overdue

        Args:
            due_time (float): the warranty time in unix format (seconds)

        Returns:
            bool: True if warranty is invalid.
        """
        current_time = time.time()
        return int(due_time - current_time) < 86400