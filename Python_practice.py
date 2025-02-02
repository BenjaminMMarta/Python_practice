#Creating a Class called "names"
class names:
  #Creating contructor with an argument "__init__"
  def __init__(self, name):
    if name == "Ben" or name == "Madalyn":
      print("Hi, my name is {}!".format(name))
    else:
      print("Please enter a name I know!")
name1 = names("Ben")
name2 = names("Madalyn")
name3 = names("Mindy")
