from profiles import profile

@profile.route("/welcome", methods=["GET"])
def welcome_result():
    return "hello welcomes you"