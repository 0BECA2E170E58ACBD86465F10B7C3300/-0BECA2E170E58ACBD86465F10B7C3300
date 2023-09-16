'''Implement a classed called player that represets a criket player. The player class; should have a
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and
Bowler from the player class. Override the play() method in each drived class to print "The batsman"
is batting " and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each objeact.'''


# Define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")
        
# Define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The  bowler is bowling.")
        
# Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("Thr bowler is bowling .")
    
# Creat objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
