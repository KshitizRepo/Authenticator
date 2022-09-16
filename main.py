from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.get("/registration")
def read_user_details(photo, name, bio, phone, email, password):
    # TODO: Add validity checks for name, phone , email and password
    # TODO: Functionality to store photo

    data = {"name": name, "bio": bio, "phone": phone, "email": email, "password": password}
    with open('user_cred.json', 'r+') as fd:
        existing_data = json.load(fd)
        existing_data["user_details"].append(data)
        fd.seek(0)
        json.dump(existing_data, fd, indent=4)
    return {"Message": "User Added Successfully"}


@app.get("/login")
def login(email, password):
    # TODO: Research on google authentication
    with open('user_cred.json', 'r+') as fd:
        existing_data = json.load(fd)
        for i in existing_data["user_details"]:
            if i["email"] == email and i["password"] == password:
                return {"Message": "Login Successfully"}
        raise HTTPException(status_code=401, detail="Login Error")
