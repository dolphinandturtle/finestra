from abstract import Buffer

class BufferPygame(Buffer):

    def __init__(self, width, height):
        self.core = pg.Surface((width, height))
        self.width = width
        self.height = height

    def blend_normal(self, other, x: int, y: int):
        self.core.blit(other, (x, y))

    def blend_add(self, other, x: int, y: int):
        raise NotImplementedError

    def blend_subtract(self, other, x: int, y: int):
        raise NotImplementedError

    def blend_multiply(self, other, x: int, y: int):
        raise NotImplementedError

    def blend_screen(self, other, x: int, y: int):
        raise NotImplementedError

    @property
    def size(self) -> (int, int):
        return (self.width, self.height)
