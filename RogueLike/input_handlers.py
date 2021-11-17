from typing import Optional

import tcod.event #importing the event system so we dont have to import the whole module

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]: #EventDispatch.ev_quit is called when you want to close the program. raising the SystemExit()
        raise SystemExit()
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]: #receives key presses and returns action subclass or None if no keys are pressed
        action: Optional[Action] = None #var action will hold the info we will later assign the Actions class

        key = event.sym #hold the key pressed. Note: doesnt record mod keys

        if key == tcod.event.K_UP: #creates MovementAction if certain keys are pressed
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE: #sends EscapeAction if esc is hit 
            action = EscapeAction()

        # No valid key was pressed
        return action
