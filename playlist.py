# # model a playlist (My Version)

# song1 = {
#     "name": "Wasted Years",
#     "Artist": ["Iron Maiden"],
#     "Album": "Somewhere in Time",
#     "Date": "1985",
#     "Duration": "3:21"
# } 
# song2 = {
#     "name": "Time After Time",
#     "Artist": ["Ozzy Osbourne"],
#     "Album": "Greatest Hits",
#     "Date": "2005",
#     "Duration": "4:03"
# } 
# song3 = {
#     "name": "Uncle Tom's Cabin",
#     "Artist": ["Warrant"],
#     "Album": "Cherry Pie",
#     "Date": "1990",
#     "Duration": "3:52"
# } 
# song4 = {
#     "name": "Each Moment Like the First",
#     "Artist": ["James Holden", "The Animal Spirits"],
#     "Album": "The Animal Spirits",
#     "Date": "2017",
#     "Duration": "3:52"
# } 






# playlist = [song1, song2, song3]
# print(playlist)

#Udemy version

playlist = {
    'name': 'patagonia bus',
    'author': 'Dirk Diggler',
    'songs': [
        {"name": "Wasted Years", "Artist": ["Iron Maiden"], "Album": "Somewhere in Time", "Date": "1985", "Duration": 3.21},
        {"name": "Smell my Feet", "Artist": ["Dwicky", "Salmon"], "Album": "Kiss my Butts", "Date": "2001", "Duration": 4.32},
        {"name": "Stuck in the Well", "Artist": ["Shameka"], "Album": "Nowhere", "Date": "2017", "Duration": 2.54}
    ] 
}

total_duration = 0
for s in playlist['songs']:
    total_duration += s['Duration']

print(total_duration)
