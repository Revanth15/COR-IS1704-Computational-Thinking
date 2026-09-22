# =====
# q2.py
# =====
# Name: Revanth Ravi
# Email ID: revanth.rs.2026

def add_first_odd_digits(str_list):
    # modify the code below
    odd_count = 0
    for str in str_list:
        for ch in str:
            if ch.isdigit() and int(ch) % 2 == 1:
                odd_count += int(ch)
                break
    return odd_count
    