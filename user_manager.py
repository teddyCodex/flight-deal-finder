from data_manager import DataManager


class User:
    def __init__(self, data_manager: DataManager) -> None:
        print("Welcome to Ubuntu6ty9's flight club")
        new_user = self.new_user()
        self.data_manager = data_manager
        data_manager.add_row(new_user)

    def new_user(self) -> dict:
        first_name = input("What is your first name?: ").title()
        last_name = input("What is your last name?: ").title()
        while True:
            email = input("What is your email?: ")
            email_confirm = input("Re-enter your email to confirm: ")
            if email == email_confirm:
                user_profile = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email,
                    }
                }
                return user_profile
            else:
                print("Email does not match. Please try again.\n")
