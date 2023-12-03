import time
import pyautogui
import mouse
import keyboard

keyboard.send("alt+tab")
time.sleep(0.3)
keyboard.send("ctrl+t")
keyboard.write("https://humanbenchmark.com/tests/sequence")
keyboard.send("enter")
time.sleep(1)
pyautogui.click(pyautogui.locateOnScreen("start.png")[0], pyautogui.locateOnScreen("start.png")[1])


def record(num_tiles, coords):
    tiles = []
    while len(tiles) < num_tiles:
        for coord_num, (x, y) in enumerate(coords):
            # if pixel is white (lit up)
            if pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                tiles.append(coord_num)

                # wait for that tile to fade so we don't add it multiple times
                while pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                    pass
    return tiles


def repeat(sequence, coords):
    # click on every tile in sequence in order
    for index in sequence:
        mouse.move(coords[index][0], coords[index][1], absolute=True)
        mouse.click()


# find 3x3 grid
grid_loc = None
while not grid_loc:
    grid_loc = pyautogui.locateOnScreen('grid.png', confidence=0.7)
xs = [int(grid_loc.left + grid_loc.width // 6 + i * grid_loc.width // 3) for i in range(3)]
ys = [int(grid_loc.top + grid_loc.height // 6 + i * grid_loc.height // 3) for i in range(3)]

# contain 9 coordinates at indexes 0-8
coords = []
for y in ys:
    for x in xs:
        coords.append((x, y))

# run the program
num_tiles = 1
while True:
    # get the sequence that the game gives us
    sequence = record(num_tiles, coords)

    # play sequence back
    repeat(sequence, coords)
    num_tiles += 1
    time.sleep(0.5)