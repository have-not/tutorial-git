def getGreetMsg(time=12):
    if (6<time and time<10):
        return "good morning!"
    else:
        return "hello!"

if (__name__ == "__main__"):
    print(getGreetMsg(12))

