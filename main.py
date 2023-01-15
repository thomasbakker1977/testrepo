# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
player_first_scored = 'Ruud Gullit'
player_second_scored = 'Marco van Basten'

goal_0 = 32
goal_1 = 45 + 9

scorers = player_first_scored + " " + str(goal_0) + ", " +  player_second_scored + " " + str(goal_1)

report = (f'{player_first_scored} scored in the {goal_0}nd minute\n{player_second_scored} scored in the {goal_1}th minute')

print(report)

#Part 2

player = 'Hans van Breukelen'
first_name =(player[0:4])
find_player_first_name = str(player.find ("Hans"))

player_last_name = (player[5:])
str(player_last_name)

last_name_len = len(player_last_name)
print (last_name_len)

name_short = ((player[0]) + ". "  + (player_last_name)) 
print (name_short)

chant = str(4 * (first_name+"! "))
chant = (chant[0:-1])
print (chant)

last_character = 32
good_chant = last_character != ord(chant[-1])
