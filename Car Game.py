user_input = ""
started = False

while user_input != "quit":
    user_input = input("> ").lower()

    if user_input == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif user_input == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif user_input == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")