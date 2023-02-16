# # Get input from the user
# seconds = int(input("Enter the number of seconds: "))

# # Convert seconds to days, hours, minutes, and seconds
# minutes, seconds = divmod(seconds, 60)
# print(divmod(seconds, 60))
# hours, minutes = divmod(minutes, 60)

# days, hours = divmod(hours, 24)

# # Print the result
# print(f"{seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")


# Get input from the user
seconds = int(input("Enter the number of seconds: "))

# Convert seconds to days, hours, minutes, and seconds
minutes = seconds // 60
print(minutes)
seconds = seconds % 60
print(seconds)
hours = minutes // 60
print(hours)
minutes = minutes % 60
days = hours // 24
hours = hours % 24

# Print the result
print(f"{seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

