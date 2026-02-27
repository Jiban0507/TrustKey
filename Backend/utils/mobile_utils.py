import re

country_rules = {
    "+91": {"name": "India", "length": 10, "start_digits": ["6","7","8","9"]},
    "+880": {"name": "Bangladesh", "length": 10, "start_digits": ["1"]},
    "+1": {"name": "USA", "length": 10, "start_digits": ["2","3","4","5","6","7","8","9"]},
    "+44": {"name": "UK", "length": [10,11], "start_digits": ["7"]},
    "+61": {"name": "Australia", "length": 9, "start_digits": ["4"]},
    "+81": {"name": "Japan", "length": [9,10], "start_digits": ["7","8","9"]},
    "+49": {"name": "Germany", "length": [10,11], "start_digits": ["1"]},
    "+33": {"name": "France", "length": 9, "start_digits": ["6"]},
    "+39": {"name": "Italy", "length": [9,10], "start_digits": ["3"]},
    "+86": {"name": "China", "length": 11, "start_digits": ["1"]},
    "+7": {"name": "Russia", "length": 10, "start_digits": ["9"]},
    "+34": {"name": "Spain", "length": 9, "start_digits": ["6","7"]},
    "+55": {"name": "Brazil", "length": [10,11], "start_digits": ["9"]},
    "+27": {"name": "South Africa", "length": 9, "start_digits": ["6","7","8"]},
    "+82": {"name": "South Korea", "length": [9,10], "start_digits": ["1"]},
    "+966": {"name": "Saudi Arabia", "length": 9, "start_digits": ["5"]},
    "+971": {"name": "UAE", "length": 9, "start_digits": ["5"]},
    "+92": {"name": "Pakistan", "length": 10, "start_digits": ["3"]},
    "+94": {"name": "Sri Lanka", "length": 9, "start_digits": ["7"]},
    "+93": {"name": "Afghanistan", "length": 9, "start_digits": ["7"]}
}

def check_mobile(mobile_number: str) -> str:
    """
    Mobile validation utility.
    Detects country code, validates length and starting digits.
    Returns ZKP-style proof message.
    """
    mobile_number = str(mobile_number).strip()

    for code, rule in country_rules.items():
        if mobile_number.startswith(code):
            local_number = mobile_number[len(code):]
            local_number = re.sub(r"\D", "", local_number)

            expected_length = rule["length"]
            if isinstance(expected_length, list):
                if len(local_number) not in expected_length:
                    return f"Proof Failed: {rule['name']} number length must be {expected_length}"
            else:
                if len(local_number) != expected_length:
                    return f"Proof Failed: {rule['name']} number length must be {expected_length}"

            if "start_digits" in rule:
                if local_number[0] not in rule["start_digits"]:
                    return f"Proof Failed: {rule['name']} number must start with {rule['start_digits']}"

            return f"Proof Verified: Valid {rule['name']} Mobile Number"

    return "Proof Failed: Unknown Country Code"