class Action:
    pass

class EscapeAction(Action): #sub-class of action
    pass

class MovementAction(Action): #sub-class of action
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
