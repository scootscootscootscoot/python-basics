
#1
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)


#2
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

#3
changed_values2 = lyrics.splitlines()
print(changed_values2)

#4
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

#5
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
# Separate the composers
composers_split = composers.split(";")
# Get the third composer
third_composer = composers_split[2]
# Find the comma in the name
comma_position = third_composer.find(',')
# Use the slicing notation to get the last name
last_name = third_composer[:comma_position]
# Use the slicing notation to get the first name
first_name = third_composer[comma_position +1:]
# Join the names to get the 3rd composer's name in "first last" format
third_composer_name = first_name + " " + last_name
# Print the composer's name
print(third_composer_name)

#6
left_padded = '        Operators are standing by'
right_padded = 'Call now          '
left_cleaned = left_padded.strip()
right_cleaned = right_padded.strip()
result = right_cleaned +"! "+left_cleaned
print(result)


#7
student_name = "Owen"
grade = 94.75
assignment_number = 12
print('Student name: %s, Assignment ID: %04d, Grade: %.2f%%' % (student_name, assignment_number, grade))

#8
employee_id = "30"
employee_id_padded = "%06d" % int(employee_id)
print(employee_id_padded)

#9
print(r"\n represents a new line")

#10
i_want_to_yell = 'yeah'
I_NEED_TO_BE_QUIET = 'SHHHHH'
this_is_a_title = 'this is a title'
sWAPcASE = 'sWAPcASE'
capitalize_this = 'capitalize this'

print(i_want_to_yell.upper())
print(I_NEED_TO_BE_QUIET.lower())
print(this_is_a_title.title())
print(sWAPcASE.swapcase())
print(capitalize_this.capitalize())