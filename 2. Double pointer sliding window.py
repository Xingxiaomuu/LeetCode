def substring_length(s):
    left = 0
    maximum_length = 0
    character_dict = {}
    for i,char in enumerate(s):
        if char in character_dict and character_dict[char]>=left:
            left = character_dict[char]+1
        character_dict[char] = i
        maximum_length = max(maximum_length,i-left+1)
    return maximum_length

def main():
    s = "abcabcbb"
    print(substring_length(s))

main()