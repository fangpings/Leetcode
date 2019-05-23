from functools import reduce

def letterCombinations(digits):
    mapping = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    return reduce(lambda ret, digit: reduce(lambda x, y: x + y, map(lambda x: [x + c for c in mapping[digit]], ret)), digits, [''])

if __name__ == '__main__':
    print(letterCombinations('23'))