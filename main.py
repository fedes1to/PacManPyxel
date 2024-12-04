import pyxel
from laberinto import Laberinto
from pacman import Pacman
from laberinto import normal_direction
from fantasma import Fantasma

class App:
    def __init__(self):
        pyxel.init(224, 280, "Pac-Man", 65, pyxel.KEY_ESCAPE, 3)
        pyxel.load("assets/theme.pyxres")
        self.laberinto = Laberinto()
        self.fantasma = Fantasma(self.laberinto, 112, 112, 0)
        self.pacman = Pacman(self.laberinto)
        pyxel.run(self.update, self.draw)

    # Devuelve False si no hay puntos en el tablero
    def draw_dots(self):
        dot_exists = False
        for column_number in range(2, len(self.laberinto.grid[0])):  # 2 = dos columnas de offset
            for line_number in range(len(self.laberinto.grid)):
                if self.laberinto.grid[line_number][column_number] == 2:
                    pyxel.rect(column_number * 8 + 3 - 16, line_number * 8 + 3, 2, 2, 15)  # -16 = dos columnas de offset
                    dot_exists = True
                elif self.laberinto.grid[line_number][column_number] == 3:
                    pyxel.blt(column_number * 8 - 16, line_number * 8, 1, 224, 0, 8, 8)  # -16 = dos columnas de offset
                    dot_exists = True
        return dot_exists

    def update(self):
        self.pacman.update()
        self.fantasma.update()

    def draw(self):
        pyxel.cls(0)
        if (self.pacman.lives == 0): # Si pacman no tiene vidas
            pyxel.text(100, 140, "GAME OVER", 7)
        elif (self.draw_dots()): # Si hay puntos en el tablero
            pyxel.blt(0, 0, self.laberinto.level_image(), 0, 0, 224, 248, 0) # Dibujamos el mapa
            self.pacman.draw_pacman()
            self.fantasma.draw_fantasma()
            pyxel.text(2, 250, "Puntaje: " + str(self.pacman.score), 7)
            pyxel.text(2, 260, "Vidas: " + str(self.pacman.lives), 7)
            pyxel.text(2, 270, "Nivel: " + str(self.laberinto.level), 7)
        elif (self.laberinto.level < 3): # Si no es el último nivel
            self.laberinto.level += 1 # Pasamos al siguiente nivel
            self.pacman.set_pacman() # Reseteamos a Pac-Man
        else: # Si llega al último nivel
            pyxel.text(100, 140, "HAS GANADO !!!", 7)


App()