def is_pangram(str):
    # a_to_z_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    current_set = set()
    for ch in str:
        if ch.isalpha():
            current_set.add(ch.lower())
    if len(current_set) == 26:
        return True
    else:
        return False
    
print(is_pangram("The quick brown fox jumps over the lazy dog."))   # True
print(is_pangram("The quick brown fox jumps over the lazy cat."))   # False
print(is_pangram("Pack my box with five dozen liquor jugs."))       # True
print(is_pangram("The five boxing wizards jump quickly."))          # True
print(is_pangram("Mr. Jock, TV quiz Ph.D., bags few lynx."))        # True