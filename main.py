# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
player_first_scored = 'Ruud Gullit'
player_second_scored = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_first_scored + " " + str(goal_0) + ", " +  player_second_scored + " " + str(goal_1)

report = f'{player_first_scored} scored in the {goal_0}nd minute\n{player_second_scored} scored in the {goal_1}th minute'

print(report)

#Part 2

player = 'Hans van Breukelen'
return_firstname_len = player.find(" ")
first_name = player[0:return_firstname_len]
print(first_name)

last_name_tmp = player[return_firstname_len:]
last_name = last_name_tmp[1:]
print (last_name)

last_name_len = len(last_name)
print (last_name_len)

name_short = ((player[0]) + ". "  + (last_name)) 
print (name_short)

#print(f"Hello, {first_name_player}!")
chant = ((f"{first_name}! ")*return_firstname_len)
chant = chant[:-1]
print (chant)

ASCII_last_character = 32
good_chant = ASCII_last_character != ord(chant[-1])
