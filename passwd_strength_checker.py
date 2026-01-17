import string

def load_common_pw(filename="common_pw.txt"):
    common = set() #empty set
    with open(filename,"r",encoding="utf-8") as f:
        for line in f:
            pw = line.strip() #clean each line i.e., removes spaces
            if pw and not pw.startswith("#"): #ignores junk lines
                common.add(pw.lower()) #store pw in lowercase
    return common

COMMON_PASSWORDS = load_common_pw()



def strong_password(pw):

    pw_clean = pw.strip() #remove unwanted spaces
    pw_lower = pw_clean.lower() #convert to lowercase

    #Block common passwords first
    if pw_lower in COMMON_PASSWORDS:
        return False
    
    return (
        len(pw_clean) >= 10 and
        any(i.isupper() for i in pw_clean) and #upper character
        any(i.islower() for i in pw_clean) and #lower character
        any(i.isdigit() for i in pw_clean) and #digit
        any(i in string.punctuation for i in pw_clean) #special character
    )

password = input("Write your password: ")

if strong_password(password):
    print("Password is strong")
else:
    print("Password is weak or too common")