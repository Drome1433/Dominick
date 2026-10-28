# Baby Prep C - Functional Baby


# Baby Poops: weight drops 5 oz
def poop(current_weight):
    current_weight -= 5
    print("Baby pooped. -5oz")
    return current_weight


# Baby Pees: weight drops 4 oz
def pee(current_weight -=4)
    current_weight -=4
    print("Baby peed. -4 oz")
    return current_weight


# Baby eats: +11 oz..Every 3rd eat triggers poop
def eat(current_weight, eat_count):
    current_weight += 11
    eat_count += 1
    print("Baby ate. +11 oz")
    if eat_count % 3 ==0:
        current_weight = poop(current_weight)
    return current_weight, eat_count


# Baby drinks: +8 oz. Every third drink triggers pee
def drink(current_weight, drink_count):
    current_weight +=8
    drink_count += 1
    print("Baby drank. +8 oz")
    if drink_count % 3 == 0:
        current_weight = pee(current_weight)
    return current_weight, drink_count


# Baby cries:mood becomes fussy
def cry ():
    print("Baby is crying! Waahhh!")
    return "fussy"


# Baby sleeps: mood becomes sleepy
def sleep():
    print("Baby is sleeping. zzzzz.....")
    return "sleepy"


# Print all tracked state. changes nothing
def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    print("--- Status ---")
    print(f"Name:   {baby_name}")
    print(f"Weight: {current_weight} oz")
    print(f"Mood:   {eat_count}")
    print(f"Eats:   {eat_count}")
    print(f"Drinks: {drink_count}")


#Ask for a starting weight; fall back to a default on bad input
def get_started_weight():
    default = 120
    raw = input(f"Starting weight in oz [{default}]: ").strip()
    if raw == "":
        return default
    try:
        weight = int(raw)
    except ValueError:
        print(f"Not a member, using {default}.")
        return default
    if weight <=0:
        print(f"Weight must be positive, using {default}.")
        return default
    return weight


#Main 
def main():
    baby_name = input("Baby name: ").strip() or "Baby"
    starting_weight = get_starting_weight()
    current_weight = starting_weight
    mooe = "calm"
    eat_count = 0 
    drink_count = 0

    print(f"\n{baby_name} is here at {starting_weight} oz!")
    print(f"Actions: eat, drink, cry, sleep, status, home")

    while True:
        action = input ("\nAction: ").strip().lower()

        if action == "eat":
            current_weight, eat_count = eat(current_weight, eat_count)
        elif action == "drink":
            current_weight, drink_count = drink(current_weight, drink_count)
        elif action == "cry":
            mood = cry()
        elif action == "sleep":
            mood = sleep()
        elif action == "status":
            display_status(baby_name, current_weight, mood, eat_count, drink_count)
        elif action == "home":
            print(f"Taking {baby_name} home. Goodbye!")
            break
        else:
            print("Unknown action. Try: eat, drink, cry, sleep, status, home")


if __name__ == "__main__":
    main()