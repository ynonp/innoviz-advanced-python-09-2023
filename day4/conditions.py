from threading import Condition, Thread
import time
import random


def printer(text: str, wait_for: Condition, notify: Condition):
    def run():
        with wait_for:
            while True:
                wait_for.wait()

                print(text)
                with notify:
                    notify.notify()
                time.sleep(random.random())
    return run


first_cw = Condition()
second_cw = Condition()
third_cw = Condition()


t1 = Thread(target=printer("*", first_cw, second_cw))
t2 = Thread(target=printer("**", second_cw, third_cw))
t3 = Thread(target=printer("***", third_cw, first_cw))

t1.start()
t2.start()
t3.start()

first_cw.acquire()
first_cw.notify()
first_cw.release()