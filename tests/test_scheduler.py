from warranty_man.scheduler import Counter
import time

DAY_SEC = 86400.0

def test_get_time_pass():
    assert isinstance(Counter().get_time(), float)

def test_unix2day():
    ten_days = DAY_SEC * 10

    assert Counter().unix2day(ten_days) == 10

def test_isdue(mocker):
    due_time = DAY_SEC * 5
    timer = Counter()
    mocker.patch.object(time, 'time', return_value=DAY_SEC * 10)

    assert timer.is_due(due_time) is True