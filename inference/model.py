
class Inference:

    def __init__(self, loop=None):
        self.loop = loop
        self.str = "Inference model for Predictive maintenance"

    def run(self, data):
        if not data:
            return False

        if isinstance(data, str):
            return True
