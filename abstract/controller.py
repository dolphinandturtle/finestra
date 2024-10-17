from enum import Enum, auto


class StateButton(Enum):
    UP = auto()
    DOWN = auto()
    PRESSED = auto()
    RELEASED = auto()


class Keyboard:

    @property
    def zero(self) -> StateButton:
        raise NotImplementedError

    @property
    def one(self) -> StateButton:
        raise NotImplementedError

    @property
    def two(self) -> StateButton:
        raise NotImplementedError

    @property
    def three(self) -> StateButton:
        raise NotImplementedError

    @property
    def four(self) -> StateButton:
        raise NotImplementedError

    @property
    def five(self) -> StateButton:
        raise NotImplementedError

    @property
    def six(self) -> StateButton:
        raise NotImplementedError

    @property
    def seven(self) -> StateButton:
        raise NotImplementedError

    @property
    def eight(self) -> StateButton:
        raise NotImplementedError

    @property
    def nine(self) -> StateButton:
        raise NotImplementedError

    @property
    def a(self) -> StateButton:
        raise NotImplementedError

    @property
    def b(self) -> StateButton:
        raise NotImplementedError

    @property
    def c(self) -> StateButton:
        raise NotImplementedError

    @property
    def d(self) -> StateButton:
        raise NotImplementedError

    @property
    def e(self) -> StateButton:
        raise NotImplementedError

    @property
    def f(self) -> StateButton:
        raise NotImplementedError

    @property
    def g(self) -> StateButton:
        raise NotImplementedError

    @property
    def h(self) -> StateButton:
        raise NotImplementedError

    @property
    def i(self) -> StateButton:
        raise NotImplementedError

    @property
    def j(self) -> StateButton:
        raise NotImplementedError

    @property
    def k(self) -> StateButton:
        raise NotImplementedError

    @property
    def l(self) -> StateButton:
        raise NotImplementedError

    @property
    def m(self) -> StateButton:
        raise NotImplementedError

    @property
    def n(self) -> StateButton:
        raise NotImplementedError

    @property
    def o(self) -> StateButton:
        raise NotImplementedError

    @property
    def p(self) -> StateButton:
        raise NotImplementedError

    @property
    def q(self) -> StateButton:
        raise NotImplementedError

    @property
    def r(self) -> StateButton:
        raise NotImplementedError

    @property
    def s(self) -> StateButton:
        raise NotImplementedError

    @property
    def t(self) -> StateButton:
        raise NotImplementedError

    @property
    def u(self) -> StateButton:
        raise NotImplementedError

    @property
    def v(self) -> StateButton:
        raise NotImplementedError

    @property
    def w(self) -> StateButton:
        raise NotImplementedError

    @property
    def x(self) -> StateButton:
        raise NotImplementedError

    @property
    def y(self) -> StateButton:
        raise NotImplementedError

    @property
    def z(self) -> StateButton:
        raise NotImplementedError

    @property
    def f1(self) -> StateButton:
        raise NotImplementedError

    @property
    def f2(self) -> StateButton:
        raise NotImplementedError

    @property
    def f3(self) -> StateButton:
        raise NotImplementedError

    @property
    def f4(self) -> StateButton:
        raise NotImplementedError

    @property
    def f5(self) -> StateButton:
        raise NotImplementedError

    @property
    def f6(self) -> StateButton:
        raise NotImplementedError

    @property
    def f7(self) -> StateButton:
        raise NotImplementedError

    @property
    def f8(self) -> StateButton:
        raise NotImplementedError

    @property
    def f9(self) -> StateButton:
        raise NotImplementedError

    @property
    def f10(self) -> StateButton:
        raise NotImplementedError

    @property
    def f11(self) -> StateButton:
        raise NotImplementedError

    @property
    def f12(self) -> StateButton:
        raise NotImplementedError

    @property
    def left(self) -> StateButton:
        raise NotImplementedError

    @property
    def right(self) -> StateButton:
        raise NotImplementedError

    @property
    def up(self) -> StateButton:
        raise NotImplementedError

    @property
    def down(self) -> StateButton:
        raise NotImplementedError

    @property
    def alt_left(self) -> StateButton:
        raise NotImplementedError

    @property
    def alt_right(self) -> StateButton:
        raise NotImplementedError

    @property
    def ctrl_left(self) -> StateButton:
        raise NotImplementedError

    @property
    def ctrl_right(self) -> StateButton:
        raise NotImplementedError

    @property
    def shift_left(self) -> StateButton:
        raise NotImplementedError

    @property
    def shift_right(self) -> StateButton:
        raise NotImplementedError


class Mouse:

    @property
    def x(self) -> int:
        raise NotImplementedError

    @property
    def y(self) -> int:
        raise NotImplementedError

    @property
    def dx(self) -> int:
        raise NotImplementedError

    @property
    def dy(self) -> int:
        raise NotImplementedError

    @property
    def left(self) -> StateButton:
        raise NotImplementedError

    @property
    def middle(self) -> StateButton:
        raise NotImplementedError

    @property
    def right(self) -> StateButton:
        raise NotImplementedError
