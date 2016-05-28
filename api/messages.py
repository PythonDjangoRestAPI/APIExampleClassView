MESSAGE = "message"

BASE_DICT = {
    MESSAGE: None
}

INVALID_EMAIL_ADDRESS_STRING = "Invalid email address"

INVALID_EMAIL_ADDRESS = {
    MESSAGE: "Invalid email address"
}

USER_ALREADY_EXISTS = {
    MESSAGE: "User with specified email already exists"
}

USER_DOES_NOT_EXISTS = {
    MESSAGE: "User does not exist."
}

USER_WITH_EMAIL_DOES_NOT_EXISTS = {
    MESSAGE: "User with specified email does not exist."
}

FACEBOOK_USER_SIGNING_WITH_EMAIL = {
    MESSAGE: "You are a Facebook User. Please use Facebook Account to login."
}

INVALID_EMAIL_OR_PASSWORD = {
    MESSAGE: "Invalid email or password"
}

INVALID_LOGIN_FOR_FACEBOOK_USER = {
    MESSAGE: "You signed up with Facebook. You cannot login "
    "using email. Try logging in with Facebook instead"
}

PASSWORD_RESET_LINK_SENT = {
    MESSAGE: "Password Reset Link sent."
}

IMAGE_UPLOAD_FAILED = {
    MESSAGE: "Image upload failed."
}

USER_NOT_FOUND = {
    MESSAGE: "User not found"
}

PASS_START_AND_END_DATE_PARAMS = {
    MESSAGE: "Pass start_date and end_date in query params"
}

NOT_MEMBER_OF_ANY_GROUP = {
    MESSAGE: "You're not a member of any group."
}

USER_FIELD_NOT_SPECIFIED = {
    MESSAGE: "'users' field not specified in the request"
}

STATUS_FIELD_NOT_SATISFIED = {
    MESSAGE: "'status' field not specified in the request"
}

NOT_MEMBER_OF_THIS_GROUP = {
    MESSAGE: "You are not the member of this group."
}

GROUP_NOTIFICATIONS_ARE_OFF = {
    MESSAGE: "Group Notifications are turned off."
}

USER_INTEGRATION_ADDDED_SUCCESSFULL = {
    MESSAGE: "Integration added successfully"
}

INTEGRITY_MESSAGE = "The fields user, app_install_time, app_local_id must make a unique set."

NO_ACTIVE_HEALTH_AGGREGATOR = {
    MESSAGE: "No active health integrations found."
}

def updateMessageDict(messageString):
    BASE_DICT[MESSAGE] = messageString
    return BASE_DICT
