import mouse
import random
import time

time.sleep(3)
origin = mouse.get_position()
bounds = (500, 500)
print(f"starting at {origin}")
last_y = origin[1]
last_x = origin[0]
while True:
    next_x = random.randint(origin[0], origin[0] + bounds[0])
    next_y = random.randint(origin[1], origin[1] + bounds[1])
    delay = (random.randint(100, 500) + random.randint(0, 500) + random.randint(0, 500) + random.randint(0, 500))/1000
    print(f"moving to ({next_y}|{next_x})")
    mouse.move(
        y=next_y,
        x=next_x,
        absolute=True,
        duration=delay)

    loc = mouse.get_position()
    if abs(loc[1] - next_y) > 10 or abs(loc[0] - next_x) > 10:
        print("EXIT BECAUSE MOUSE WAS MOVED")
        exit(0)
    delay = (random.randint(100, 200) + random.randint(0, 100) + random.randint(0, 100) + random.randint(0, 100)) / 1000
    time.sleep(delay)
    last_y = next_y
    last_x = next_x
