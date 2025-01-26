class Trail():
    def __init__(self, dest, len = 0):
        self.dest = dest
        self.len= len
    
    def describe_trail(self): 
        """Prints the description of the trail."""
        desc =f"This trail goes to {self.dest}."
        if self.len:
            desc += f"\n The trail is {self.len}km."
            \
        print(desc)
        
# Testing the method.
if __name__ == "__main__":
    my_trail = Trail("Mountain Peak", 5)
    my_trail.describe_trail()