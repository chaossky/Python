from core.base import Base

class Test(Base):
    def initialize(self):
        print("Initializing program...")
    
    def update(self):
        #print("Updating program...")
        pass

# instantiate this class and run the program
if __name__ == "__main__":
    Test().run()
