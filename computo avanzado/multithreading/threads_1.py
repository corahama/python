import threading

custom_list = []
def count(initial, final, step):
    custom_list.append([x for x in range(initial, final+1, step)])

if __name__ == "__main__":
    proc = 4
    ub = 100

    threads = []
    for i in range(1, proc+1):
        threads.append(threading.Thread(target=count, args=(i, ub, proc)))
        threads[-1].start()

    for i in threads:
        i.join()
    
    print('\n'.join(str(val) for val in custom_list))