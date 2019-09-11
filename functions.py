import hashlib
ALPHABET = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789!@#$%^&*()-_')

def initializeDb(db):
    with open('db.txt', 'r', newline='') as csv_file:
        for line in csv_file:
            line = line.strip().split(",")
            db[line[0]] = [line[1], line[2]]

def storeInfo(service, emailUser, pw, db,s):
    file = open("[your storage file here]", "a", encoding='utf-8')
    userHash = hashlib.sha256(emailUser)
    userHash = userHash.hexdigest()
    try:
        if db[service][0] == str(userHash):
            print("We already have information for this account.")
    except:
        pwHash = hashlib.sha256(pw)
        pwHash = pwHash.hexdigest()
        db[service] = [str(userHash), str(pwHash)]
        s.append(service)

        file.write(service + "," + str(userHash) + "," + str(pwHash) + '\n')
        file.close()

def checkDatabase(service, emailUser, pw, db):
    userHash = hashlib.sha256(emailUser)
    userHash = userHash.hexdigest()
    pwHash = hashlib.sha256(pw)
    pwHash = pwHash.hexdigest()
    try:
        if str(userHash) == db[service][0]:
            pass
        else:
            print("Email is incorrect.")
            return
    except:
        pass

    try:
        if db[service][1] == str(pwHash):
            print("Your password is correct.")
        else:
            print("Your password is incorrect")
    except:
        print("Service not in our database.")

def changeInfo(service, emailUser, pw, db):
    try:
        if db[service]:
            userHash = hashlib.sha256(emailUser)
            userHash = userHash.hexdigest()
            pwHash = hashlib.sha256(pw)
            pwHash = pwHash.hexdigest()


            db[service][0] = str(userHash)
            db[service][1] = str(pwHash)

    except:
        print("Service not in our database.")
def removeFromDb(service, db,s):
    try:
        if db[service]:
            del db[service]
            del s[s.index(service)]
    except:
        print("Service not in database.")

# def get_hexdigest(service, pw):
#     return str(hashlib.sha256(service + pw).hexdigest())

def makePassword(service, pw):
    key = '3leeth4x0r'.encode('utf-8')
    salt = hashlib.sha256(key + service).hexdigest()
    hash = hashlib.sha256(key + pw).hexdigest()
    return ''.join((salt, hash))

def generatePassword(service, pw, length, alphabet=ALPHABET):
    hexDigest = makePassword(service, pw)

    # Convert the hexdigest into decimal
    num = int(hexDigest, 16)

    # What base will we convert `num` into?
    num_chars = len(alphabet)

    # Build up the new password one "digit" at a time,
    # up to a certain length
    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(alphabet[idx])

    return ''.join(chars)
