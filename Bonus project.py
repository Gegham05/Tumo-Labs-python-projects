import time
print("--- Welcome to the Bonus Game! ---")
t = input("Insert time to count down (h:m:s): ")
h, m, s = map(int, t.split(":"))

seconds = h * 3600 + m * 60 + s
while seconds > 0:
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    print(f"{h:02d}:{m:02d}:{s:02d}")
    time.sleep(1)
    seconds -= 1

print("Time is over!")