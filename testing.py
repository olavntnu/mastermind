def placePins(code, guess):

        whiteCount = 0

        subtractedList = [x-y for x,y in zip(code,guess)]

        newCode = []
        newGuess = []

        for i in range(len(subtractedList)):
            if subtractedList[i] != 0:
                newCode.append(code[i])
                newGuess.append(guess[i])
        while len(newGuess) != 0:
            if newGuess[0] in newCode:
                whiteCount += 1
                newCode.remove(newGuess[0])
            newGuess.pop(0)

    
        return [subtractedList.count(0), whiteCount]

test_cases = [
    {'code': [1, 2, 3, 4], 'guess': [1, 2, 3, 4], 'expected_pins': [4, 0]},  # All correct, black pins = 4, white pins = 0
    {'code': [1, 2, 3, 4], 'guess': [4, 3, 2, 1], 'expected_pins': [0, 4]},  # All correct, but in reverse order
    {'code': [1, 2, 3, 4], 'guess': [1, 3, 2, 4], 'expected_pins': [2, 2]},  # 2 correct color and position, 2 correct color but wrong position
    {'code': [1, 2, 3, 4], 'guess': [5, 6, 7, 8], 'expected_pins': [0, 0]},  # None correct
    {'code': [1, 1, 2, 2], 'guess': [1, 2, 1, 2], 'expected_pins': [2, 2]},  # 2 correct color and position, 2 correct color but wrong position
]

for test_case in test_cases:
    code = test_case['code']
    guess = test_case['guess']
    expected_pins = test_case['expected_pins']
    
    result = placePins(code, guess)
    
    print(f"Code: {code}, Guess: {guess}, Expected Pins: {expected_pins}, Result: {result}")