#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


def main():
    width, height = 80, 50
    
   

    tileset = tcod.tileset.load_tilesheet( #sets and loads the tilemap
        "tilemap.png",32,8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(width / 2), int(height / 2), "@", (255, 255, 255))
    npc = Entity(int(width / 2 - 5), int(height / 2), "N", (255, 255, 0))
    entities = {npc, player}

    with tcod.context.new_terminal( #creates terminal instance
        width,
        height,
        tileset=tileset,
        title="~!Runic!~",
        vsync=True
    ) as context:
        root_console = tcod.Console(width, height,  order="F") #creates console that will be drawn to
        while True: #main gameloop
            root_console.print(x=player.x , y=player.y , string=player.char, fg=player.color) #draws the @ to the center of the terminal
            context.present(root_console) #updates the terminal
            root_console.clear()

            for event in tcod.event.wait(): #same as for event in pygame.event.get():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy) 
                elif isinstance(action, EscapeAction):
                    raise SystemExit()

    #only runs the main function when running the script
if __name__ == "__main__":
    main()
