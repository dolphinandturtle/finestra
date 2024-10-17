from . import Buffer

class Window:

    def blit(self, buffer: Buffer, x: int, y: int):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    @property
    def size(self) -> (int, int):
        return (self.width, self.height)

    @property
    def width(self) -> int:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError

    @property
    def title(self) -> str:
        raise NotImplementedError
