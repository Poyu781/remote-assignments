import threading
from time import sleep, time


def do_job(number):
    sleep(1.2)
    print(f"Job {number} finished")

threads = []
# rewrite everything inside this main function and keep others untouched
def main():
    start_time = time()
    for i in range(5):
        threads.append(threading.Thread(target = do_job, args = (i,)))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print("test")
    print(time() - start_time)



# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束


main()
