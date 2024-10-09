
#
# Complete the 'newPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def newPassword(a, b):
    result = ''
    for l1, l2 in zip(a,b):
        result += l1+l2
    
    if len(a) > len(b):
        result += a[len(b):]
    elif len(a) < len(b):
        result += b[len(a):]
    else:
        return result

    return result
    


if __name__ == '__main__':
    sys.stdin = open(f'test_cases/{re.sub(".py", ".txt", os.path.basename(__file__))}', 'r')

    a = input()

    b = input()

    result = newPassword(a, b)

    fptr.write(result + '\n')

    fptr.close()
