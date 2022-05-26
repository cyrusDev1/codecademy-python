authors = """Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"""

author_names = authors.split(",")
names = []
for users in author_names:
  names = names + users.split(" ")
string = ""
for i in range(len(names)):
  if i % 2 != 0:
    string = string + names[i] + " "
author_last_names = string.split(" ")
author_last_names.pop()
print(author_last_names)