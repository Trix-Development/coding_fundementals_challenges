# Convert Hours and Minutes into Seconds

# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
# Examples

# convert(1, 3) ➞ 3780

# convert(2, 0) ➞ 7200

# convert(0, 0) ➞ 0

# Notes

#     Don't forget to return the result.
#     If you get stuck on a challenge, find help in the Resources tab.
#     If you're really stuck, unlock solutions in the Solutions tab.

def convert(hours,minutes):
  seconds_in_hour = 3600
  calc1 = hours * seconds_in_hour
  second_in_min = 60
  calc2 = second_in_min * minutes
  return calc1 + calc2

print(str(convert(1,3)) + " Seconds")