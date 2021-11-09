class Sample:
    def __init__(self):
        super(Sample)
        self._action = None
    
    def print_message(self, message):
        print(message)
        
    def perform(self, action):
        pass

    def perform(self, perform_action):
        self._action = perform_action

sample1 = Sample()
sample1.print_message("Hello World")
sample1.perform("some text")
