from multiprocessing import Pool

def count(initial, final, step):
    return [x for x in range(initial, final+1, step)]

if __name__ == "__main__":
    proc = 4
    ub = 10000

    pool = Pool(proc)

    results = [pool.apply_async(count, args=(i, ub, proc, )) for i in range(1, proc+1)]
    pool.close()
    pool.join()

    print(sorted([e for element in results for e in element.get()]))
