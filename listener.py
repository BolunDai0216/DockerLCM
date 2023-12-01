import select
import time

import lcm

from exlcm import example_t


def my_handler(channel, data):
    msg = example_t.decode(data)
    print('Received message on channel "%s"' % channel)
    print("   timestamp   = %s" % str(msg.timestamp))
    print("   position    = %s" % str(msg.position))
    print("   orientation = %s" % str(msg.orientation))
    print("   ranges: %s" % str(msg.ranges))
    print("   name        = '%s'" % msg.name)
    print("   enabled     = %s" % str(msg.enabled))
    print("")


def main():
    lc = lcm.LCM()
    subscription = lc.subscribe("EXAMPLE", my_handler)

    try:
        while True:
            file_descriptor = lc.fileno()

            # Waiting for reading readiness (data available)
            ready_to_read, _, _ = select.select([file_descriptor], [], [], 0.02)

            if len(ready_to_read) != 0:
                lc.handle()
            else:
                print(f"[{time.time()}]: \t No data available")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
