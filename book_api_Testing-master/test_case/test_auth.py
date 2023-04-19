import pytest
import json
import requests
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import testDataGen

data = {
    "clientName": testDataGen.nameLen(),
    "clientEmail": testDataGen.emailgen()
}


def test_token_gen():
    LogGen.loggen().info("************Test_Auth_URL***********")
    response = requests.post(ReadConfig.getAuth(), json=data)
    global token
    token = (json.loads(response.text)["accessToken"])
    print(token)
    assert response.status_code == 201
    LogGen.loggen().info("************Test_Auth_URL_Passed***********")


def test_token_gen_alredy_used_email():
    LogGen.loggen().info("************Test_Auth_URL_gen_alredy_used_email***********")
    response = requests.post(ReadConfig.getAuth(), json=data)
    assert response.status_code == 409
    LogGen.loggen().info("************Test_Auth_URl_gen_alredy_used_email_passed***********")
