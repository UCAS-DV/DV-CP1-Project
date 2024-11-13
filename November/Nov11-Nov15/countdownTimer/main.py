import time

print("~-~-~-~-~-Timer~-~-~-~-~-")

while True:
    try:
        seconds = int(input("How long (in seconds) will your timer last? "))
    except:
        print('Invalid Amount of Time')
        continue

    for i in range(0, seconds):
        print(f'Seconds Remaining: {seconds - i}')
        time.sleep(1)

    print("\nTime's Up!")

    continue_confirmation = input('\nDo you wish to set another timer? If not, type "leave" and if so type anything: ')

    if continue_confirmation == "leave":
        exit()