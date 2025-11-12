print("--- DELIVERY SERVICE FOR RIWI CODERS ---")
print("Context: You are a Riwi student and you’re hungry")
print("Shifts available:")
print("Morning: 6:00 AM – 2:00 PM (Break: 10:30 AM – 11:30 AM)")
print("Afternoon: 2:00 PM – 10:00 PM (Break: 6:30 PM – 7:30 PM)")
print("Restaurant opens at 1:00 PM and closes at 9:00 PM")
print("Rule: Delivery takes 1 hour to arrive, and you need at least 30 minutes to eat\n")


def start_order():
    while True:
        try:
            print("\n--- Shifts ---\n1. Morning shift\n2. Afternoon shift\n")

            shift = input("Are you in the morning or afternoon shift?: ").strip()

            if shift == "1":
                morning_shift()

            elif shift == "2":
                afternoon_shift()

            else:
                print("Invalid option, choose 1 or 2")

        except ValueError:
            print("Invalid digit, choose 1 or 2")


def morning_shift():
    print("\n--- MORNING SHIFT ---")

    try:
        hour = float(input("What time is it? (In 24-hour format): "))

        if hour < 13.00:
            print("The restaurant is closed, you have to wait until 1:00 PM")

        elif 13.00 <= hour <= 20.00:
            print("The restaurant is open and you can order")
            make_order()

        elif hour >= 21.00:
            print("The restaurant is closed")

        else:
            print("Invalid time")

    except ValueError:
        print("Enter a valid time")


def afternoon_shift():

    print("\n--- AFTERNOON SHIFT ---")

    try:
        hour = float(input("\nWhat time is it? (In 24-hour format): "))

        if hour < 13.00:
            print("The restaurant is closed, you have to wait until 1:00 PM")

        elif 13.00 <= hour <= 18.00:
            print("The restaurant is open and you can order")
            make_order()

        elif 18.00 < hour < 21.00:
            print("Too late for you to order")

        elif hour >= 21.00:
            print("The restaurant is already closed")

        else:
            print("Invalid time")

    except ValueError:
        print("Enter a valid time")


def make_order():

    print("\n--- Menu ---\n1. Menú del día\n2. Bandejas\n3. Sopas\n")

    menu = input("What do you want to order?: ").strip()

    if menu == "1":
        print("\nSending a WhatsApp message to the restaurant to make your order...")
        print("\n--- Ticket ---\n1 Menú del día = 15.000\nTotal = 15.000")
        pay_order()

    elif menu == "2":
        order = input("Do you want a drink? (y/n): ")

        if order.lower == "y":
            print("\nSending a WhatsApp message to the restaurant to make your order...")
            print("\n--- Ticket ---\n1 Bandeja = 10.000\n1 Jugo = 3.000\nTotal = 13.000")
            pay_order()

        elif order.lower == "n":
            print("\nSending a WhatsApp message to the restaurant to make your order...")
            print("\n--- Ticket ---\n1 Bandeja = 10.000\nTotal = 10.000")
            pay_order()

    elif menu == "3":
        order = input("Do you want a drink? (y/n): ")

        if order.lower == "y":
            print("\nSending a WhatsApp message to the restaurant to make your order...")
            print("\n--- Ticket ---\n1 Sopa = 5.000\n1 Jugo = 3.000\nTotal = 8.000")
            pay_order()

        elif order.lower == "n":
            print("\nSending a WhatsApp message to the restaurant to make your order...")
            print("\n--- Ticket ---\n1 Sopa = 5.000\nTotal = 5.000")
            pay_order()


def pay_order():
    # print("Waiting for the delivery (takes 1 hour)...")

    while True:
        try:

            transfer = input("\nDo you want to pay by transfer? (y/n): ").lower()

            if transfer == "y":
                print("\nYour order is confirmed and paid")
                print("Waiting for the delivery (takes 1 hour)...")

            elif transfer == "n":
                print("\nYou’ll pay in cash when the delivery arrives")
                print("Waiting for the delivery (takes 1 hour)...")

            else:
                print("\nEnter a valid option (y or n)")
                continue

            answer = input("\nDid the delivery arrive? (y/n): ").lower()

            if answer == "y":
                if transfer == "y":
                    print("We hope you will enjoy your food, have a nice day")
                    break

                elif transfer == "n":
                    print(
                        "You receive your food and pay in cash, enjoy your food, have a nice day")
                    break

                else:
                    print("\nEnter a valid option (y or n)")
                    continue

            elif answer == "n":
                print("\nThe delivery didn’t arrive, you send a complaint to the restaurant")

                if transfer == "y":
                    print("Restaurant response: We’ll refund your transfer payment, sorry fot the inconvenient")
                    break

                elif transfer == "n":
                    print("Restaurant response: Sorry for the issue you'll have a 50% discount coupon")
                    break

                else:
                    print("\nEnter a valid option (y or n)")
                    continue

        except ValueError:
            print("Invalid data")

start_order()
