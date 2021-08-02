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

def main():
    pass

if __name__ == "__main__":
    main()