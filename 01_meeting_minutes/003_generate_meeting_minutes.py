import datetime
from calendar import monthrange

def last_thursday_of_month(year, month):
    # Find the last day of the month
    last_day = monthrange(year, month)[1]
    # Create a date object for the last day of the month
    last_date = datetime.date(year, month, last_day)
    # Calculate the last Thursday of the month
    return last_date - datetime.timedelta(days=(last_date.weekday() - 3) % 7)

# Load the list of secretaries
with open('001_secretaries.txt', 'r') as file:
    secretaries = file.read().splitlines()

# Load the list of committee members
with open('002_committee_members.txt', 'r') as file:
    committee_members = file.read().splitlines()

# Determine the next meeting date (last Thursday of the current month)
today = datetime.date.today()
next_meeting = last_thursday_of_month(today.year, today.month)
if today > next_meeting:
    # If today's date is past the last Thursday, calculate for the next month
    next_month = today.month + 1 if today.month < 12 else 1
    next_year = today.year if today.month < 12 else today.year + 1
    next_meeting = last_thursday_of_month(next_year, next_month)

# Find the next secretary in the rotation
secretary_index = (next_meeting.month - 1) % len(secretaries)  # simple rotation based on month
secretary_name = secretaries[secretary_index]

# Create the meeting minutes markdown file
file_name = next_meeting.strftime('%Y-%m-%d.md')
attendees_list = '\n'.join(f"- {name}" for name in committee_members)
template = f"""# Meeting Minutes for {next_meeting.strftime('%Y-%m-%d')}

## Secretary
- {secretary_name}

## Attendees
{attendees_list}

## Agenda

## Notes

## Action Items

"""

# Write the template to the markdown file
with open(file_name, 'w') as file:
    file.write(template)

print(f"Created minutes file: {file_name} with secretary: {secretary_name}")
