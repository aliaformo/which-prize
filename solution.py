points = 174

## set prize to default value of None
prize = None


## use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

## use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)

# Output: Congratulations! You won a wafer-thin mint!


'''First set prize to None and then update it only if falls into a bracket that results in winning a prize. This is accomplished in the first if statement. We then use the truth value of prize to assign result to a message based on whether a prize was won.
When prize = "penguin", or any other non-empty string, then the if prize condition is True!'''