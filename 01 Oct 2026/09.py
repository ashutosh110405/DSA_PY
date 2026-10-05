def count_characters(s: str):
    vowels = "aeiouAEIOU"
    v_count = c_count = d_count = s_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
        elif char.isdigit():
            d_count += 1
        else:
            s_count += 1
            
    return {"Vowels": v_count, "Consonants": c_count, "Digits": d_count, "Special": s_count}

# Example usage:
print(count_characters("Hello World! 123"))