#import gspread and google-auth
import gspread
from google.oauth2.service_account import Credentials

# scope lists the API that program should access, to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

""" used below code to check if the API is working
sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
"""
def get_sales_data():
    """
    gets sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be in six numbers, seperated by commas")
    print("Example: 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    inside the try, converts all string values into integers.
    Raises valueerror if strings cannot be converted into integers,
    or i there are not exactly six numbers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly six values are required, only {len(values)} were provided"
            )
    except ValueError as e:
        print(f"Invalid data: {e} , please try again.")


get_sales_data()