from Routines import ColorLogger
from Routines import measure_speed


logger = ColorLogger(filename="Playground/mylog.log")


@measure_speed(repeat_count=3, test_count=1_000_000)
def test():
    for x in range(100):
        # logger.warning("dit is een test")
        pass


logger.warning("dit is een test")
test()
