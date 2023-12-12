#Clase boton para el juego 

class Boton():
    def __init__(self, pos, texto, fuente, color_base, color_sombra):
        self.posicion_x = pos[0]
        self.posicion_y = pos[1]
        self.fuente = fuente
        self.color_base, self.color_sombra = color_base, color_sombra
        self.texto = texto
        self.text = self.fuente.render(self.texto, True, self.color_base)
        self.text_rect = self.text.get_rect(center=(self.posicion_x, self.posicion_y))

    def update(self, pantalla):
        pantalla.blit(self.text, self.text_rect)


    def check(self, pos):
        if pos[0] in range(self.text_rect.left, self.text_rect.right) and pos[1] in range(self.text_rect.top, self.text_rect.bottom):
            return True
        return False

