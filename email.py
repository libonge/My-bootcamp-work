
class Email:
    emails = []  # Initialize an empty list to store the emails.

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Initialize the 'has_been_read' attribute.

    @classmethod
    def add_email(cls, email):
        cls.emails.append(email)  # Add an email to the list.

    @classmethod
    def get_unread_emails(cls):
        return [email for email in cls.emails if not email.has_been_read]  # Return a list of unread emails.

    def read_email(self):
        self.has_been_read = True  # Mark the email as read.
        return self  # Return the email object.

def populate_emails():
    email1 = Email("sender1@example.com", "First Email", "Content 1")
    email2 = Email("sender2@example.com", "Second Email", "Content 2")
    email3 = Email("sender3@example.com", "Third Email", "Content 3")

    Email.add_email(email1)
    Email.add_email(email2)
    Email.add_email(email3)

def list_emails():
    for i, email in enumerate(Email.emails):
        print(f"{i+1}. {email.subject_line}")

def read_email(index):
    email = Email.emails[index - 1]
    email.read_email()
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    print(f"Has been read: {email.has_been_read}")

populate_emails()

while True:
    user_choice = int(input(''' Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application
    Enter selection: '''))

    if user_choice == 1:
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)

    elif user_choice == 2:
        unread_emails = Email.get_unread_emails()
        for email in unread_emails:
            print(email.subject_line)

    elif user_choice == 3:
        break  # Exit the application.

    else:
        print("Oops - incorrect input.")  # Incorrect input.

