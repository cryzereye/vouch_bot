class Vouch:
    global user, vouches
    
    def __init__(self, user, vouches=[]) -> None:
        self.user = user
        self.vouches = vouches

    def getUser() -> str:
        return user

    def getVouches():
        return vouches