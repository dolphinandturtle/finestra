class Buffer:

    def blend_normal(self, other, x: int, y: int):
        raise NotImplementedError

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

    @property
    def width(self) -> int:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError
