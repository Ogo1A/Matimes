import time

def digital_clock():
    while True:
        # Get the current time
        current_time = time.localtime()
        # Format the time as HH:MM:SS
        time_str = time.strftime("%H:%M:%S", current_time)
        
        # Clear the console (works for Windows CMD and most *nix terminals)
        print("\033[H\033[J", end="")
        
        # Print the time in a digital clock format
        print("┌──────────┐")
        print(f"│ {time_str} │")
        print("└──────────┘")
        
        # Wait for 1 second before updating
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()
