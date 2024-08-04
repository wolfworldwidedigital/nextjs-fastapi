import stytch
from fastapi import FastAPI
import dotenv

app = FastAPI()
@app.get("/api/python")

def login():
        return {"message": "Login please"}

client = stytch.Client(
    project_id="NEXT_PUBLIC_STYTCH_PUBLIC_TOKEN",
    secret="STYTCH_SECRET",
)


login_or_create_resp = client.magic_links.email.login_or_create(
    email="sandbox@stytch.com",
    login_magic_link_url="https://localhost:3000/authenticate",
    signup_magic_link_url="https://localhost:3000/authenticate",
)
# Responses are fully-typed `pydantic` objects
print(login_or_create_resp)

auth_resp = client.magic_links.authenticate(
    token="DOYoip3rvIMMW5lgItikFK-Ak1CfMsgjuiCyI7uuU94=",
)
print(auth_resp)