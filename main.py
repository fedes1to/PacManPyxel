import pyxel
from laberinto import Laberinto
from pacman import Pacman
from frutas import Frutas
from fantasma import Fantasma
import time

class App:
    def __init__(self):
        pyxel.init(224, 260, "Pac-Man", 65, pyxel.KEY_ESCAPE, 3)
        pyxel.load("assets/theme.pyxres")
        self.laberinto = Laberinto()
        self.pacman = Pacman(self.laberinto)
        self.frutas = Frutas(self.laberinto)
        self.fantasmas = []

        # Inicializamos los 4 fantasmas
        for i in range(4):
            self.fantasmas.append(Fantasma(self.laberinto, self.pacman, i))

        self.minutos_finales, self.segundos_finales = -1, -1
        pyxel.run(self.update, self.draw)

    # Devuelve False si no hay puntos en el tablero
    def draw_dots(self):
        dot_number = 0
        for column_number in range(2, len(self.laberinto.grid[0])):  # 2 = dos columnas de offset
            for line_number in range(len(self.laberinto.grid)):
                if self.laberinto.grid[line_number][column_number] == 2:
                    pyxel.rect(column_number * 8 + 3 - 16, line_number * 8 + 3, 2, 2, 15)  # -16 = dos columnas de offset
                    dot_number += 1
                elif self.laberinto.grid[line_number][column_number] == 3:
                    pyxel.blt(column_number * 8 - 16, line_number * 8, 1, 224, 0, 8, 8)  # -16 = dos columnas de offset
                    dot_number += 1
        return dot_number

    def update(self):
        self.pacman.update()
        for fantasma in self.fantasmas:
            fantasma.update()
        self.frutas.check_colision(self.pacman)

    def get_final_time(self):
        if (self.minutos_finales == -1 or self.segundos_finales == -1):
            tiempo_total = pyxel.frame_count / 60
            self.minutos_finales = int(tiempo_total // 60)
            self.segundos_finales = int(tiempo_total % 60)

    def draw(self):
        pyxel.cls(0)

        dots_left = -1

        # Escena de Game Over
        if (self.pacman.lives < 1): # Si pacman no tiene vidas
            # Inicializamos el tiempo final
            self.get_final_time()

            pyxel.text(100, 50, "GAME OVER", 7)
            pyxel.text(100, 70, "Tiempo: " + str(self.minutos_finales) + "m " + str(self.segundos_finales) + "s", 7)
            pyxel.blt(75, 150, 0, 32, 16, 32, 32, scale=4, rotate=45, colkey=0) # El Pac-Man del final
        else:
            dots_left = self.draw_dots()
        
        if dots_left > 0: # Si hay puntos en el tablero
            pyxel.blt(0, 0, self.laberinto.level_image(), 0, 0, 224, 248, 0) # Dibujamos el mapa
            # Si se ha comido una cantidad de puntos y no hay frutas en el tablero
            if ((dots_left == 70 or dots_left == 170) and (len(self.frutas.posicion_frutas) == 0)):
                # Spawneamos una fruta aleatoria
                self.frutas.spawn_fruta(dots_left == 70)
            self.pacman.draw_pacman()
            self.frutas.draw_fruits()
            for fantasma in self.fantasmas:
                fantasma.draw_fantasma()
            pyxel.text(2, 251, "Vidas: " + str(self.pacman.lives), 7)
            pyxel.text(40, 251, "Nivel: " + str(self.laberinto.level), 7)
            pyxel.text(80, 251, "Puntaje: " + str(self.pacman.score), 7)
        elif (self.laberinto.level < 3): # Si no es el último nivel
            time.sleep(2) # Esperamos 2 segundos para que la transición sea más suave
            self.laberinto.level += 1 # Pasamos al siguiente nivel
            self.pacman.set_pacman() # Reseteamos a Pac-Man
            for fantasma in self.fantasmas:
                fantasma.set_fantasma()
            self.frutas.reset_frutas() # Reseteamos las frutas
        # Si llega al último nivel y no está Pac-Man muerto
        elif (self.laberinto.level == 3 and dots_left != -1):
            # Inicializamos el tiempo final
            self.get_final_time()
            
            pyxel.text(100, 50, "HAS GANADO !!!", 7)
            pyxel.text(100, 60, "Vidas: " + str(self.pacman.lives), 7)
            pyxel.text(100, 70, "Tiempo: " + str(self.minutos_finales) + "m " + str(self.segundos_finales) + "s", 7)
            pyxel.blt(75, 150, 0, 32, 16, 32, 32, scale=4, rotate=45, colkey=0) # El Pac-Man del final


App()