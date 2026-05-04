import datetime

print("--- TORNADO ANALYZER BOOTING UP ---")
print("Type 'quit' at any time to exit.\n")

while True:
    mph_input = input("Enter tornado wind speed in mph (or 'quit'): ")
    if mph_input.lower() == 'quit':
        break

    try:
        mph = float(mph_input)
    except ValueError:
        print("❌ Error: Please enter a valid number (e.g. 120.5). Try again.\n")
        continue

    kmh = mph * 1.60934

    nu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    RESET = "\033[0m"
    RED = "\033[31m"
    ORANGE = "\033[38;5;214m"
    YELLOW = "\033[93m"
    GREEN = "\033[32m"
    PURPLE = "\033[35m"
    BLUE = "\033[34m"

    if mph < 65:
        status, color = "Gale", BLUE
    elif 65 <= mph <= 85:
        status, color = "EF0", BLUE
    elif 86 <= mph <= 110:
        status, color = "EF1", GREEN
    elif 111 <= mph <= 135:
        status, color = "EF2", YELLOW
    elif 136 <= mph <= 165:
        status, color = "EF3", ORANGE
    elif 166 <= mph <= 200:
        status, color = "EF4", RED
    else:
        status, color = "EF5", PURPLE

    print(f"\n[{nu}] {color}ANALYSIS:{RESET}")
    print(f"Speed: {round(kmh, 1)} km/h ({mph} mph) | Class: {color}{status}{RESET}")

    with open("tornado_log.txt", "a") as file:
        file.write(f"[{nu}] Speed: {mph} mph | Class: {status}\n")
    
    print("-> Data saved to tornado_log.txt")
    print("-" * 45 + "\n")

print("Program closed. Log updated.")