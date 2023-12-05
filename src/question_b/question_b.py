#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(string1, string2):
    indexes = []
    for i in range(len(string1)):
        if string1[i:i+len(string2)] == string2: 
            indexes.append(i+1)

    return tuple(indexes)

def validate_string1(string):
    if len(string) < 8 or len(string) > 16:
        return "Invalid"

def validate_substring(string):
    if len(string) < 4 or len(string) > 4:
        return "Invalid"
    

