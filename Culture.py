import requests
import datetime

class Event:
    def __init__(self, name, start_time, end_time, location):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
class Content:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

class EventManagementSystem:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_events(self, start_date, end_date):
        url = f"https://example.com/api/events?key={self.api_key}&start_date={start_date}&end_date={end_date}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Unable to fetch events from API.")
        events_data = response.json()
        events = []
        for event_data in events_data:
            name = event_data['name']
            start_time = datetime.datetime.strptime(event_data['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(event_data['end_time'], '%Y-%m-%d %H:%M:%S')
            location = event_data['location']
            events.append(Event(name, start_time, end_time, location))
        return events

    def schedule_event(self, event):
        url = f"https://example.com/api/schedule?key={self.api_key}"
        data = {
            "name": event.name,
            "start_time": event.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": event.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            "location": event.location
        }
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise ValueError("Unable to schedule event using API.")
        return response.json()

    def get_contents(self, start_date, end_date):
        url = f"https://example.com/api/contents?key={self.api_key}&start_date={start_date}&end_date={end_date}"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Unable to fetch contents from API.")
        contents_data = response.json()
        contents = []
        for content_data in contents_data:
            title = content_data['title']
            description = content_data['description']
            url = content_data['url']
            contents.append(Content(title, description, url))
        return contents

    def create_content(self, content):
        url = f"https://example.com/api/create_content?key={self.api_key}"
        data = {
            "title": content.title,
            "description": content.description,
            "url": content.url
        }
        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise ValueError("Unable to create content using API.")
        return response.json()

# Integrated Testing
def test_event_management_system():
    # Test fetching events
    api_key = "12345"
    ems = EventManagementSystem(api_key)
    start_date = datetime.date.today().strftime('%Y-%m-%d')
    end_date = (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    events = ems.get_events(start_date, end_date)
    assert len(events) > 0, "No events found."
    # Test scheduling an event
    event = Event("Test Event", datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(hours=1), "Test Location")
    ems.schedule_event(event)

def test_get_content():
    content = get_content()
    assert len(content) == 100, 'Should return 100 contents'
    assert content[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'Should return correct content title'
    print('Content Management Test Passed!')

if __name__ == '__main__':
    test_event_management_system()
    test_get_content()

