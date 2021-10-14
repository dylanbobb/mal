import readline

def READ(str):
    return str

def EVAL(str):
    return str

def PRINT(str):
    return str

def rep(str):
    return PRINT(EVAL(READ(str)))

def main():
    while True:
        try:
            line = input("user> ")
            print(rep(line))
        except EOFError:
            break

if __name__ == "__main__":
    main()