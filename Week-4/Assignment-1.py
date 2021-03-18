import threading
from time import sleep,time

def do_job(number):
    sleep(5)
    print(f"Job {number} finished")
# rewrite everything inside this main function and keep others untouched
def main():
    start_time = time()
    for i in range(5):
        x = threading.Thread(target=do_job,args=(i,))
        x.start()
    x.join()
    print("f")
    # 等到全部子 Thread 執行完後，才去計算時間
    print(time()-start_time)

main()


