import time

import lcm

from exlcm import example_t


def main():
    msg = example_t()
    msg.timestamp = 0
    msg.position = (1, 2, 3)
    msg.orientation = (1, 0, 0, 0)
    msg.ranges = range(15)
    msg.num_ranges = len(msg.ranges)
    msg.name = "example string"
    msg.enabled = True

    lc = lcm.LCM()

    while True:
        lc.publish("EXAMPLE", msg.encode())
        time.sleep(0.01)
        msg.timestamp = int(time.time())


if __name__ == "__main__":
    main()
