*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  shinji
    Set Password  shinji99
    Set Password Confirmation  shinji99
    Click Button  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  qw
    Set Password  qwerty123
    Set Password Confirmation  qwerty123
    Click Button  Register
    Registration Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  qwerty
    Set Password  qw1
    Set Password Confirmation  qw1
    Click Button  Register
    Registration Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
    Set Username  qwerty
    Set Password  qwertyuiop
    Set Password Confirmation  qwertyuiop
    Click Button  Register
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  qwerty
    Set Password  qwerty123
    Set Password Confirmation  qwerty456
    Click Button  Register
    Registration Should Fail With Message  Password confirmation doesn't match password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Click Button  Register
    Registration Should Fail With Message  Username is already taken

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
