from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    # Future DOB check
    if birth_date > today:
        return None

    # Special case: DOB == today
    if birth_date.date() == today.date():
        return 0  # newborn

    age = today.year - birth_date.year
    # Adjust if birthday has not occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def check_age(dob):
    """
    Accepts DOB in either DD-MM-YYYY or YYYY-MM-DD format.
    Returns age category based on DOB.
    """
    try:
        # Try DD-MM-YYYY first
        try:
            birth_date = datetime.strptime(dob, "%d-%m-%Y")
        except ValueError:
            birth_date = datetime.strptime(dob, "%Y-%m-%d")

        age = calculate_age(birth_date)
        if age is None:
            return "Proof Failed: DOB cannot be in the future"
        if age > 120:
            return "Proof Failed: Unrealistic Age"

        # Age ranges
        if age == 0:
            return "Proof Verified: User is Newborn (0 days old)"
        elif age < 13:
            return "Proof Verified: User is Child (0-12)"
        elif 13 <= age < 18:
            return "Proof Verified: User is Teenager (13-17)"
        elif 18 <= age < 30:
            return "Proof Verified: User is Young Adult (18-29)"
        elif 30 <= age < 60:
            return "Proof Verified: User is Middle-aged Adult (30-59)"
        else:
            return "Proof Verified: User is Senior Citizen (60+)"
    except:
        return "Proof Failed: Invalid DOB format, use DD-MM-YYYY or YYYY-MM-DD"


def age_range_proof(dob, min_age=None, max_age=None):
    """
    ZKP-style range proof:
    Returns True if user's age is within given range,
    without revealing exact age.
    Accepts DOB in DD-MM-YYYY or YYYY-MM-DD format.
    """
    try:
        try:
            birth_date = datetime.strptime(dob, "%d-%m-%Y")
        except ValueError:
            birth_date = datetime.strptime(dob, "%Y-%m-%d")

        age = calculate_age(birth_date)
        if age is None:
            return "Proof Failed: DOB is in the future"

        if min_age is not None and age < min_age:
            return f"Proof Failed: Age < {min_age}"
        if max_age is not None and age > max_age:
            return f"Proof Failed: Age > {max_age}"

        return "Proof Verified: Age is within range"
    except:
        return "Proof Failed: Invalid DOB format"


def future_age(dob, future_year):
    """
    Predicts user's age in a given future year.
    Accepts DOB in DD-MM-YYYY or YYYY-MM-DD format.
    """
    try:
        try:
            birth_date = datetime.strptime(dob, "%d-%m-%Y")
        except ValueError:
            birth_date = datetime.strptime(dob, "%Y-%m-%d")

        today = datetime.now()
        if birth_date > today:
            return "Proof Failed: DOB cannot be in the future"

        age_in_future = future_year - birth_date.year
        # Adjust if birthday has not occurred yet in the future year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_in_future -= 1

        if age_in_future < 0:
            return f"Proof Failed: In {future_year}, DOB is invalid (future birth)."
        return f"Proof Verified: In {future_year}, user will be {age_in_future} years old."
    except:
        return "Proof Failed: Invalid DOB format"