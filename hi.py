def find_dog(sound):
    if sound == "멍멍":
        return("개가 짖네")

    else:
        return("다른 동물이구나")

sound = "멍멍"
find_result = find_dog(sound)

print(find_result)


def _myFunction(x):
    return 2*x+1

result = _myFunction(99)
print(result)