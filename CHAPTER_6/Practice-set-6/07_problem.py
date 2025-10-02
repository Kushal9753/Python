"""Write a program to find out whether a given post is talking about "Kushal" or not."""

post =input("Enter the post ")

if("Kushal".lower() in post.lower()):
  print("this post is talking about kushal")
else:
  print("This post is not taking about kushal ")