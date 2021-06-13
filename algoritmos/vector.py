import time
start = time.time()

x=25
c = [[0,0,0],[0,0,0],[0,0,0]]
end = 'false'
for i in range(0,10):
    c[0][0] = i
    if end == 'true':
        break
    for i in range(0,10):
        c[0][1] = i
        if end == 'true':
            break
        for i in range(0,10):
            c[0][2] = i
            if end == 'true':
                break
            for i in range(0,10):
                c[1][0] = i
                if end == 'true':
                    break
                for i in range(0,10):
                    c[1][1] = i
                    if end == 'true':
                        break
                    for i in range(0,10):
                        c[1][2] = i
                        if (c[0][0] + c[0][1] + c[0][2])==x and (c[1][0] + c[1][1] + c[1][2]) == x :
                            print(c[0])
                            print(c[1])
                            print(c[2])
                            end = 'true'
                            break


end = time.time()
print(end - start)
