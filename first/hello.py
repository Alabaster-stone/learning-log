def main():
    name = input("what's your name? ")
    hello(name)
    hello()

def hello(to="max"):
    print("hello,",to)

main()