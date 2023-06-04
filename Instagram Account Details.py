import instaloader
ig = instaloader.Instaloader()
user_name = input("Enter the username :")
profile = instaloader.Profile.from_username(ig.context,user_name)
print("Username :",profile.username)
print(profile.username," has uploaded ",profile.mediacount ,"posts")
print(profile.username, "has", str(profile.followers), "followers")
print(profile.username, "follows", str(profile.followees), "people")
print("Bio :",profile.biography)


