import onlinepayment
import pay_details
import pay_details.secure_pay
import pay_details.my_Test
from secrets import compare_digest
import requests.sessions
import email_validator
mail_id = "youremail@gmail.com"
number_code = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
letter_code = 'a, b, c, d, e, f'


class Pay(onlinepayment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pay_details = pay_details
        self.pay_details.secure_pay = pay_details.secure_pay

    def pay(self):
        return self.pay()


def validate_email_id(email_id):
    """

    :type email_id: Email ID
    """
    try:
        email_validator.validate_email(email_id)
    except email_validator.EmailNotValidError as e:
        print(str(e))
    else:
        return False


while True:
    email_id = input("Enter your email id: ")
    if validate_email_id(email_id):
        print("Email is not valid. Please")
        continue
    else:
        print("Email is Valid")
        break


def create_token(token_number_code):
    token_number_code = int(token_number_code)
    return token_number_code


def send_token(email_id, phone_number):
    if email_id is None:
        raise Exception("Email id is not valid")
    elif phone_number is None:
        raise Exception("Phone number is not valid")
    else:
        print("Token is sent to your email id and phone number")
        return email_id, phone_number


@property
def get_card_details(card_number, card_name, card_cvv, card_expiry_date):
    if card_number is None:
        raise Exception("Card number is not valid")
    elif card_number == card_name:
        raise Exception("Card name is not valid")
    while card_cvv >= 4:
        if card_cvv < 4:
            raise Exception("Card cvv is not valid")
        if card_number >= 16:
            raise Exception("Card number is not valid")
    card_expiry_date = int(card_expiry_date)
    if card_expiry_date.strftime("%Y-%m"):
        return card_expiry_date
    elif card_expiry_date is None:
        raise Exception("Invalid card expiry date")


@property
def validatePin_password_token(token, password, pin):
    while compare_digest(token, int(token)):
        if compare_digest(token, int(token)):
            continue
        else:
            token.verify()
            while compare_digest(password, pin):
                if not password.verify():
                    raise Exception("Password is not valid")
                password = str(password)
            else:
                raise Exception("Pin is not valid")


@property
def get_card_type(credit_card, debit_card):
    for card_details in credit_card:
        if get_card_details(card_details, debit_card):
            while credit_card.verify(card_details):
                return True
            else:
                if debit_card.verify(card_details[0]):
                    return card_details.verify()


class create_sessions_for_payments:
    def create_session(self, payments):
        error_codes = {
            "Transaction ErrorCode": 592,
            "No Transaction Found": 200,
            "Transaction in Progress": 409,
            "Transaction notApproved": 100
        }
        for error_code in error_codes:
            if error_code.startswith("5"):
                return error_codes[::1]

        requests.Session.session = self
        if payments is None:
            raise Exception("No Payments done during transaction")
