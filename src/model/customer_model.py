class Customer:
    pass
    def __init__(self, username, full_name, year_of_birth, password, email, create_at, update_at):
        self.username = username
        self.full_name = full_name
        self.year_of_birth = year_of_birth
        self.password = password
        self.email = email
        self.created_at = create_at
        self.updated_at = update_at

    def __str__(self):
        return f'{self.username} {self.full_name} {self.year_of_birth} {self.email} {self.created_at} {self.updated_at}'