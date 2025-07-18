## Define Functions
def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow.")

def green_light():
    print("Go! The light is green.")

## Create a Function to Control the Traffic Light
def traffic_light(state):
    state = state.lower()
    
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
   ## Handle Invalid States
    else:
        print(f"Error: Invalid state '{state}'. Please use 'red', 'yellow', or 'green'.")


## Test the function with different states
traffic_light("red")
traffic_light("yellow")
traffic_light("green")
traffic_light("blue")  ## Invalid state test