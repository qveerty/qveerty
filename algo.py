"""
from PIL import Image
import os


def _split(values: list, lenght: int) -> list[list[int]]:
    for i in range(0, len(values), lenght):
        yield values[i: i + lenght]
            

def compression(pixels: list, resolution: tuple, cfn: str) -> str:
    LENGHT: int = resolution[0]
    lines = list(_split(pixels, LENGHT))
    ...
    print(f'Data compression operation finished.\nFile Compressed: {cfn}')



def main() -> str:
    file = input('File Name: ')
    cfn_ = input('Compressed File Name: ')
    if os.path.isfile(file):
        try:
            image = Image.open(file)
            match image.mode:
                case 'L':
                    compression(list(image.getdata()), image.size, cfn_)
                    image.close()
                case _:
                    os.system('cls')
                    print('This algorithm works only with W\B images.')
                    #to do: add converting mode
        except Exception as e:
            print(f'{e}')
    else:
        print(f'"{file}" does not exists.')


if __name__ == '__main__':
    os.system('cls')
    main()
"""
    
# The following code is only a test
a = [24, 24, 24, 24, 9, 9, 9]

def fix(l: list[int]) -> list[tuple[int]]:
    index = 0
    fixed = []
    for n in l:
        fixed.append((n, index))
        index += 1
    return fixed

new_list = fix(a)

def _next(index: int, _list: list[tuple[int]]) -> int:
    return _list[index + 1][0]

def count(fixed_list: list[tuple[int]]) -> list[int]:
    counter = 0
    for t in fixed_list:
        t: tuple[int]
        if t[0] != _next(fixed_list.index(t), fixed_list):
            return [(t[0], counter + 1)]
        else:
            counter += 1
            continue

x = count(new_list)
print(new_list)
print(x)
