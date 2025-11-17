def format_name(full_name):
    """
    Formats a full name into 'Last, First' format.
    The function splits the name into parts and uses:
    - the first word as the first name,
    - the last word as the last name.
    """
    parts = full_name.strip().split()
    if len(parts) == 0:
        return ""
    
    first = parts[0]
    last = parts[-1]
    
    return f"{last}, {first}"
# Example usage:
print(format_name("John Doe"))        
print(format_name("  Alice   Wonderland  "))
print(format_name("SingleName"))
print(format_name("Mary Ann Smith"))


