import time
start = time.time()

# x = int(input('Introduce un numero: '))
x=4
c = [[0,0,0],[0,0,0],[0,0,0]]
c1 = c[0][0] + c[0][1] + c[0][2]
c2 = c[1][0] + c[1][1] + c[1][2]
c3 = c[2][0] + c[2][1] + c[2][2]
c4 = c[0][0] + c[1][0] + c[2][0]
c5 = c[0][1] + c[1][1] + c[2][1]
c6 = c[0][2] + c[1][2] + c[2][2]
c7 = c[0][0] + c[1][1] + c[2][2]
c8 = c[2][0] + c[1][1] + c[0][2]
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
                        if end == 'true':
                            break
                        for i in range(0,10):
                            c[2][0] = i
                            if end == 'true':
                                break
                            for i in range(0,10):
                                c[2][1] = i
                                if end == 'true':
                                    break
                                for i in range(0,10):
                                    c[2][2] = i
                                    if (c[0][0] + c[0][1] + c[0][2])==x and (c[1][0] + c[1][1] + c[1][2]) == x and (c[2][0] + c[2][1] + c[2][2]) == x and (c[0][0] + c[1][0] + c[2][0]) == x and (c[0][1] + c[1][1] + c[2][1]) == x and (c[0][2] + c[1][2] + c[2][2]) == x and (c[0][0] + c[1][1] + c[2][2]) == x and (c[2][0] + c[1][1] + c[0][2]) == x:
                                        print(c[0])
                                        print(c[1])
                                        print(c[2])
                                        end = 'true'
                                        break

end = time.time()
print(end - start)
