square_size = int(input('give square size: '))
commands = input('give space separated commands: ').split()

i = j = 0 # starting point; i is x axis and j is y axis

def check_quality(x):
    if x < 0:
        return 0
    elif x > square_size-1:
        return square_size-1
    else:
        return x

for command in commands:
    if command == 'up':
        j -= 1
        j = check_quality(j)
    elif command == 'down':
        j += 1
        j = check_quality(j)
    elif command == 'left':
        i -= 1
        i = check_quality(i)
    elif command == 'right':
        i += 1
        i = check_quality(i)
    else:
        break

print(i * square_size + j)
