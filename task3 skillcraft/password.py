import re
import getpass  # for hidden password input

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Numbers check
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Strength result
    if strength_points == 5:
        return "Strong Password 💪", feedback
    elif 3 <= strength_points < 5:
        return "Moderate Password ⚡", feedback
    else:
        return "Weak Password ❌", feedback


# Run the tool (hidden input)
password = getpass.getpass("Enter your password : ")
strength, issues = check_password_strength(password)

print("\nPassword Strength:", strength)
if issues:
    print("Suggestions:")
    for issue in issues:
        print("-", issue)