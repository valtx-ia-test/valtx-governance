import json  # REQ-EXP-001
from datetime import datetime, timedelta  # REQ-EXP-001

def export_user_data(user_data):  # REQ-EXP-001
    """Generates a JSON file with user personal data."""
    # Validate user_data structure here if needed  # REQ-EXP-001
    json_data = json.dumps(user_data)  # REQ-EXP-001
    with open('user_data_export.json', 'w') as json_file:  # REQ-EXP-001
        json_file.write(json_data)  # REQ-EXP-001

def calculate_deadline(request_date):  # REQ-EXP-002
    """Calculates the deadline for data export response."""
    # Ensure request_date is a datetime object  # REQ-EXP-002
    if isinstance(request_date, str):  # REQ-EXP-002
        request_date = datetime.strptime(request_date, '%Y-%m-%d')  # REQ-EXP-002
    deadline = request_date + timedelta(days=10)  # REQ-EXP-002
    return deadline.strftime('%Y-%m-%d')  # REQ-EXP-002

if __name__ == "__main__":  # REQ-EXP-001
    # Example usage  # REQ-EXP-001
    user_data_example = {  # REQ-EXP-001
        "id": 123,  # REQ-EXP-001
        "name": "John Doe",  # REQ-EXP-001
        "email": "john.doe@example.com"  # REQ-EXP-001
    }  # REQ-EXP-001
    export_user_data(user_data_example)  # REQ-EXP-001
