from scripts.run_setup import User


class AuthorizingProcess:
    def __init__(self, session):
        self.session = session

    def create_new_account(self, username, password):
        if self.session.query(User).filter_by(name=username).first():
            return "Username already exists"

        new_user = User(name=username)
        new_user.set_password(password)

        self.session.add(new_user)
        self.session.commit()

        return "Account created successfully"

    def log_in(self, username, password):
        user = self.session.query(User).filter_by(name=username).first()

        if user and user.check_password(password):
            return "Login successful"
        else:
            return "Invalid username or password"