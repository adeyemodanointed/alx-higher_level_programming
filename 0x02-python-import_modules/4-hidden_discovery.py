#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for value in dir(hidden_4):
        if(not value.startswith("__")):
            print(value)
