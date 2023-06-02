from datetime import datetime, timedelta, timezone

# PVP Schedule
rotation = ['Seal Rock', 'Fields of Glory (Shatter)', 'Onsal Hakair']

today = datetime.now(tz=timezone.utc)
origin = datetime.fromtimestamp(1683986401, tz=timezone.utc)
delta = (today - origin)
offset = delta.days%3

print("Today's FFXIV PVP map is "+rotation[offset]+". \nThe PVP schedule is as follows: Seal Rock, Fields of Glory (Shatter), Onsal Hakair.")