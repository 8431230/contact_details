import sys

def safe_int(v, d):
    try:
        return int(v)
    except:
        return d

def safe_str(v, d):
    if v.strip() == "":
        return d
    return v

if len(sys.argv) == 6:
    script = sys.argv[0]
    name = safe_str(sys.argv[1], "Unknown")
    phone = safe_int(sys.argv[2], 9999999999)
    email = safe_str(sys.argv[3], "not_provided@email.com")
    city = safe_str(sys.argv[4], "Unknown City")
    user_type = safe_str(sys.argv[5], "auto")
    print("user provided input values:")
else:
    script = sys.argv[0]
    name = "soumya"
    phone = 9876543210
    email = "soumya@gmail.com"
    city = "Hubballi"
    user_type = "auto"
    print("no input given - using default values:")

if user_type == "auto":
    if city.lower() == "hubballi":
        contact_priority = "Local Contact"
    else:
        contact_priority = "Non-Local Contact"
else:
    contact_priority = user_type

print("\n--- Contact Details Result ---")
print("script name :", script)
print("name :", name)
print("phone :", phone)
print("email :", email)
print("city :", city)
print("contact priority :", contact_priority)
