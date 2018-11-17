*** Settings ***
Library    AppiumLibrary

*** Keywords ***
[Documentation] This KW will scroll to given element in a page, and will stop and fail if scroll to the end of page without given element present
Scroll Down to Element
    [Arguments]                         ${element}
    # base case for dealing no element (empty page) case
    ${no_element}               Run Keyword And Return Status    Page Should Contain Element    id=noElementText
    Return From Keyword If      ${no_element}==${TRUE}    None

    ${element_present}          Set Variable    ${FALSE}
    ${temp_first_element}       Get Text    xpath=//android.widget.TextView[@resource-id='${PACKAGE}:id/element_name'][1]

    :FOR    ${i}    IN RANGE    0    50
    \    ${element_present}          Run Keyword And Return Status    Page Should Contain Element    xpath=//android.widget.TextView[@resource-id='${PACKAGE}:id/element_name'][@text='${element}']
    \    Run Keyword If              ${element_present} == ${TRUE}    Exit For Loop
    \
    \    Swipe Up                    xpath=//*
    \
    \    ${current_first_element}    Get Text    xpath=//android.widget.TextView[@resource-id='${PACKAGE}:id/channel_name'][1]
    \    Run Keyword If              '${temp_first_element}' == '${current_first_element}'    Exit For Loop
    \
    \    ${temp_first_element}       Set Variable    ${current_first_element}

    Run Keyword If    ${element_present} == ${FALSE}    Fail    msg=Element not found in this page
