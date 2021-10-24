import json

with open("user_data.json", "r") as userDataFile:
    dataSet = json.loads(userDataFile.read())

def check_for_match(username, password, dataSet):

    if (username, password) in dataSet.items():
        return "correct username and password"

    elif username in dataSet.keys():
        return "incorrect password"

    elif username not in dataSet.keys():
        return "username not found"

def register_user(username, password, dataSet):
    dataSet.update({username: password})
    dataSet = json.dumps(dataSet, indent=4)
    with open("user_data.json", "w") as userDataFile:
        userDataFile.write(dataSet)

def main():
    pass

if __name__ == "__main__":
    main()
