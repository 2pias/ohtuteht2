*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  newuser  newpassword1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  existinguser  password123
    Input Register Command
    Input Credentials  existinguser  newpassword1
    Output Should Contain  User with username existinguser already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ab  validpassword1
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  invalid!user  validpassword1
    Output Should Contain  Username must consist only of letters a-z

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  validuser  sho1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  validuser  onlyletters
    Output Should Contain  Password must not consist only of letters
