from time import sleep

def loop():
    print("0%   ○○○○○", end="")
    sleep(0.9)
    print("\r", end="")

    print("20%  ◍○○○○", end="")
    sleep(0.9)
    print("\r", end="")

    print("40%  ◍◍○○○", end="")
    sleep(0.9)
    print("\r", end="")

    print("60%  ◍◍◍○○", end="")
    sleep(0.9)
    print("\r", end="")

    print("80%  ◍◍◍◍○", end="")
    sleep(0.9)
    print("\r", end="")

    print("100% ◍◍◍◍◍", end="")
    sleep(0.9)
    print("\r", end="")

while True:
    loop()


