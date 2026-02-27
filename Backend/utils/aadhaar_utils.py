def check_aadhaar(aadhaar_number: str) -> str:
    """
    Aadhaar validation utility.
    Checks if Aadhaar number is 12 digits, all numeric, and not starting with 0.
    Returns ZKP-style proof message.
    """
    if aadhaar_number.isdigit() and len(aadhaar_number) == 12 and not aadhaar_number.startswith("0"):
        return "Proof Verified: Valid Aadhaar Number"
    else:
        return "Proof Failed: Invalid Aadhaar Number"