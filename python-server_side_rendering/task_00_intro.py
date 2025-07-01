import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print('Template is empty, no output files generated.')
        return

    if not isinstance(attendees, list):
        print('No data provided, no output files generated.')
        return

    if not template.strip():
        print('template must not be empty')
        return

    if not len(attendees):
        print('attendees must not be empty')
        return

    for i, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee[key]
            if value is None:
                value = f'{key}:N/A'
            invitation = invitation.replace(f"{{{key}}}", str(value))

        fileName = f'output_{i}.txt'

        try:
            if not os.path.exists(fileName):
                with open(fileName, 'w') as f:
                    f.write(invitation)
                    print(f'Invitation written to {fileName}')
        except Exception as e:
            print(f"Error writing {fileName}: {e}")



with open('template.txt', 'r') as f:
        template = f.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


generate_invitations(template, attendees)