import timeit
import myasync

def python_print_result(n):
    print(f"[Python] I slept for {n} seconds")


print(myasync.run(python_print_result))


