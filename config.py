import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8649011888:AAG9yiHYgex9uxXm6T4ah6BeYnSOiNPxZn4")

# Multiple admins support
ADMIN_IDS: list[int] = [
    int(x.strip()) 
    for x in os.getenv("ADMIN_IDS", "1899208318,8045127644,515858240").split(",")
    if x.strip().isdigit()
]

print(f"Loaded {len(ADMIN_IDS)} admin(s): {ADMIN_IDS}")
