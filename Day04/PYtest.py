def userID(str1):

    #rules
    #1. user id can contain alpha numeric
    #2. user id can't cantain spcial char except '_'
    #3. user id should not start from a number
    #4. user id should min contain 8 chars following the above policy

    if len(str1) >= 8:
        if str1.isalnum():
            if str1[0] == '_' or (ord(str1[0]) >= 65 and ord (str1[0]) <= 90) or (ord(str1[0]) >= 97 and ord(str1[0]) <= 122):
                return f"{str1} is meeting all the policy"
            else:
                return f"{str1} userid should start with alphanum or '_'"
        else:
            return f"{str1} userid should not contain sp chars expect '_'"
    else:
        return f"{str1} userid should contain min of 8 characters"


print(userID("_sanjeev"))