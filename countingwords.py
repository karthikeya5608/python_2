
def fun():
    inputc=input("enter:")
    charactercount=0
    for i in inputc:
        words=inputc.split(" ")
        charactercount=len(words)
    print(charactercount)
fun()