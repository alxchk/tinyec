# -*- coding: utf-8 -*-
import random
import math
import sys

if sys.version_info.major > 2:
    xrange = range

    def to_bytes(value):
        values = []
        while value:
            values.append(value % 256)
            value = value >> 8
        return bytes(values)

else:
    def to_bytes(value):
        bytes = []
        while value:
            bytes.append(chr(value % 256))
            value = value >> 8
        return b''.join(bytes)


_COMB_IDX = (
    3, 2, 1,
    5, 4, 1,
    6, 4, 2,
    7, 4, 3,
    9, 8, 1,
    10, 8, 2,
    11, 8, 3,
    12, 8, 4,
    13, 8, 5,
    14, 8, 6,
    15, 8, 7,
    17, 16, 1,
    18, 16, 2,
    19, 16, 3,
    20, 16, 4,
    21, 16, 5,
    22, 16, 6,
    23, 16, 7,
    24, 16, 8,
    25, 16, 9,
    26, 16, 10,
    27, 16, 11,
    28, 16, 12,
    29, 16, 13,
    30, 16, 14,
    31, 16, 15,
    33, 32, 1,
    34, 32, 2,
    35, 32, 3,
    36, 32, 4,
    37, 32, 5,
    38, 32, 6,
    39, 32, 7,
    40, 32, 8,
    41, 32, 9,
    42, 32, 10,
    43, 32, 11,
    44, 32, 12,
    45, 32, 13,
    46, 32, 14,
    47, 32, 15,
    48, 32, 16,
    49, 32, 17,
    50, 32, 18,
    51, 32, 19,
    52, 32, 20,
    53, 32, 21,
    54, 32, 22,
    55, 32, 23,
    56, 32, 24,
    57, 32, 25,
    58, 32, 26,
    59, 32, 27,
    60, 32, 28,
    61, 32, 29,
    62, 32, 30,
    63, 32, 31,
    65, 64, 1,
    66, 64, 2,
    67, 64, 3,
    68, 64, 4,
    69, 64, 5,
    70, 64, 6,
    71, 64, 7,
    72, 64, 8,
    73, 64, 9,
    74, 64, 10,
    75, 64, 11,
    76, 64, 12,
    77, 64, 13,
    78, 64, 14,
    79, 64, 15,
    80, 64, 16,
    81, 64, 17,
    82, 64, 18,
    83, 64, 19,
    84, 64, 20,
    85, 64, 21,
    86, 64, 22,
    87, 64, 23,
    88, 64, 24,
    89, 64, 25,
    90, 64, 26,
    91, 64, 27,
    92, 64, 28,
    93, 64, 29,
    94, 64, 30,
    95, 64, 31,
    96, 64, 32,
    97, 64, 33,
    98, 64, 34,
    99, 64, 35,
    100, 64, 36,
    101, 64, 37,
    102, 64, 38,
    103, 64, 39,
    104, 64, 40,
    105, 64, 41,
    106, 64, 42,
    107, 64, 43,
    108, 64, 44,
    109, 64, 45,
    110, 64, 46,
    111, 64, 47,
    112, 64, 48,
    113, 64, 49,
    114, 64, 50,
    115, 64, 51,
    116, 64, 52,
    117, 64, 53,
    118, 64, 54,
    119, 64, 55,
    120, 64, 56,
    121, 64, 57,
    122, 64, 58,
    123, 64, 59,
    124, 64, 60,
    125, 64, 61,
    126, 64, 62,
    127, 64, 63,
    129, 128, 1,
    130, 128, 2,
    131, 128, 3,
    132, 128, 4,
    133, 128, 5,
    134, 128, 6,
    135, 128, 7,
    136, 128, 8,
    137, 128, 9,
    138, 128, 10,
    139, 128, 11,
    140, 128, 12,
    141, 128, 13,
    142, 128, 14,
    143, 128, 15,
    144, 128, 16,
    145, 128, 17,
    146, 128, 18,
    147, 128, 19,
    148, 128, 20,
    149, 128, 21,
    150, 128, 22,
    151, 128, 23,
    152, 128, 24,
    153, 128, 25,
    154, 128, 26,
    155, 128, 27,
    156, 128, 28,
    157, 128, 29,
    158, 128, 30,
    159, 128, 31,
    160, 128, 32,
    161, 128, 33,
    162, 128, 34,
    163, 128, 35,
    164, 128, 36,
    165, 128, 37,
    166, 128, 38,
    167, 128, 39,
    168, 128, 40,
    169, 128, 41,
    170, 128, 42,
    171, 128, 43,
    172, 128, 44,
    173, 128, 45,
    174, 128, 46,
    175, 128, 47,
    176, 128, 48,
    177, 128, 49,
    178, 128, 50,
    179, 128, 51,
    180, 128, 52,
    181, 128, 53,
    182, 128, 54,
    183, 128, 55,
    184, 128, 56,
    185, 128, 57,
    186, 128, 58,
    187, 128, 59,
    188, 128, 60,
    189, 128, 61,
    190, 128, 62,
    191, 128, 63,
    192, 128, 64,
    193, 128, 65,
    194, 128, 66,
    195, 128, 67,
    196, 128, 68,
    197, 128, 69,
    198, 128, 70,
    199, 128, 71,
    200, 128, 72,
    201, 128, 73,
    202, 128, 74,
    203, 128, 75,
    204, 128, 76,
    205, 128, 77,
    206, 128, 78,
    207, 128, 79,
    208, 128, 80,
    209, 128, 81,
    210, 128, 82,
    211, 128, 83,
    212, 128, 84,
    213, 128, 85,
    214, 128, 86,
    215, 128, 87,
    216, 128, 88,
    217, 128, 89,
    218, 128, 90,
    219, 128, 91,
    220, 128, 92,
    221, 128, 93,
    222, 128, 94,
    223, 128, 95,
    224, 128, 96,
    225, 128, 97,
    226, 128, 98,
    227, 128, 99,
    228, 128, 100,
    229, 128, 101,
    230, 128, 102,
    231, 128, 103,
    232, 128, 104,
    233, 128, 105,
    234, 128, 106,
    235, 128, 107,
    236, 128, 108,
    237, 128, 109,
    238, 128, 110,
    239, 128, 111,
    240, 128, 112,
    241, 128, 113,
    242, 128, 114,
    243, 128, 115,
    244, 128, 116,
    245, 128, 117,
    246, 128, 118,
    247, 128, 119,
    248, 128, 120,
    249, 128, 121,
    250, 128, 122,
    251, 128, 123,
    252, 128, 124,
    253, 128, 125,
    254, 128, 126,
    255, 128, 127,
    257, 256, 1
)


def from_bytes(bytes):
    return sum(
        (
            byte if isinstance(byte, int) else ord(byte)
        ) * (256**i) for i, byte in enumerate(bytes)
    )


def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    g, g1 = a, b
    while g1:
        q = g // g1
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        g, g1 = g1, g - q * g1
    return g, u, v


def mod_inv(a, p):
    if a < 0:
        return p - mod_inv(-a, p)
    g, x, y = egcd(a, p)
    if g != 1:
        raise ArithmeticError("Modular inverse does not exist")
    else:
        return x % p


class Curve(object):
    __slots__ = ('name', 'a', 'b', 'field', 'g', 'bytes', 'bits')

    def __init__(self, a, b, field, name="undefined"):
        self.name = name
        self.a = a
        self.b = b
        self.field = field
        self.bytes = (int(math.log(self.field.p, 2)) + 7) // 8
        self.bits = self.bytes * 8
        self.g = Point(self, self.field.g[0], self.field.g[1])

    def is_singular(self):
        return (4 * self.a**3 + 27 * self.b**2) % self.field.p == 0

    def on_curve(self, x, y):
        return (y**2 - x**3 - self.a * x - self.b) % self.field.p == 0

    def __eq__(self, other):
        if not isinstance(other, Curve):
            return False
        return \
            self.a == other.a and self.b == other.b and \
            self.field == other.field

    def __hash__(self):
        return hash((self.a, self.b, self.field, self.bits, self.g))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "\"%s\" => y^2 = x^3 + %dx + %d (mod %d)" % (
            self.name, self.a, self.b, self.field.p)


class SubGroup(object):
    __slots__ = ('p', 'g', 'n', 'h')

    def __init__(self, p, g, n, h):
        self.p = p
        self.g = g
        self.n = n
        self.h = h

    def __eq__(self, other):
        if not isinstance(other, SubGroup):
            return False
        return \
            self.p == other.p and self.g == other.g and \
            self.n == other.n and self.h == other.h

    def __hash__(self):
        return hash((self.p, self.g, self.n, self.h))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Subgroup => generator %s, order: %d, "\
          "cofactor: %d on Field => prime %d" % (
              self.g, self.n, self.h, self.p)

    def __repr__(self):
        return self.__str__()


class Point(object):
    __slots__ = ('curve', 'x', 'y', 'p', 'inf', '_pc')

    def __init__(self, curve, x=None, y=None, inf=None, pc=None):
        self.curve = curve
        self.p = self.curve.field.p

        if x is not None and x > self.p:
            x %= self.p

        if y is not None and y > self.p:
            y %= self.p

        self.x = x
        self.y = y
        self.inf = not (
            x is not None and y is not None
        ) if inf is None else inf
        self._pc = pc

    def precompute(self):
        items = 2**8
        pc = [None]*(items)
        portion = self.curve.bits // 8

        pc[0] = Point(self.curve)
        pc[1] = self.copy()

        prev = pc[1]

        for i in xrange(1, 8):
            elem = prev.copy()

            for _ in xrange(portion):
                elem._double()

            prev = pc[1 << i] = elem

        for i in xrange(items - 8 - 1):
            t_idx = _COMB_IDX[i*3 + 0]
            f_idx = _COMB_IDX[i*3 + 1]
            s_idx = _COMB_IDX[i*3 + 2]

            pc[t_idx] = pc[f_idx]+pc[s_idx]

        self._pc = pc

    def copy(self):
        return Point(
            self.curve,
            None if self.inf else self.x,
            None if self.inf else self.y,
            self.inf,
            self._pc
        )

    def __neg__(self):
        if self.inf:
            return Point(self.curve)

        return Point(
            self.curve, self.x,
            (-self.y) % self.p,
            self.inf, self._pc)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False

        if other.inf and self.inf:
            return True

        if other.inf != self.inf:
            return False

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((
            self.curve, self.x, self.y,
            self.p, self.inf, self._pc
        ))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if self.inf:
            return other.copy()

        result = self.copy()
        result += other
        return result

    def __sub__(self, other):
        if self.inf:
            return other.copy()

        other = -other
        return self + other

    def __iadd__(self, other):
        if self._pc:
            self._pc = None

        if other.inf:
            pass
        elif self.inf:
            self.inf = other.inf
            self.x = other.x
            self.y = other.y
        elif self.x == other.x and self.y != other.y:
            self.inf = True
        elif self == other:
            self._double()
        else:
            m = self.y - other.y
            m *= mod_inv(self.x - other.x, self.p)

            x_r = m**2
            x_r -= self.x
            x_r -= other.x
            x_r %= self.p

            m *= (x_r - self.x)

            self.y += m
            self.y = -self.y
            self.y %= self.p
            self.x = x_r

        return self

    def _double(self):
        if self.inf:
            return

        if self._pc:
            self._pc = None

        m = self.x ** 2
        m *= 3
        m += self.curve.a
        m *= mod_inv(self.y*2, self.p)

        x_r = m**2
        x_r -= self.x
        x_r -= self.x
        x_r %= self.p

        m *= (x_r - self.x)

        self.y += m
        self.y = -self.y
        self.y %= self.p
        self.x = x_r

    def _comb(self, k):
        result = Point(self.curve)
        portions = self.curve.bits // 8

        for d in xrange(portions-1, -1, -1):
            idx = 0
            for i in xrange(8):
                bit_idx = i*portions + d
                bit = (k >> bit_idx) & 1
                idx |= bit << i

            result._double()
            result += self._pc[idx]

        return result

    def __mul__(self, other):
        x1 = None

        if other % self.curve.field.n == 0:
            return Point(self.curve)

        elif other > 0 and self._pc:
            return self._comb(other)

        if other < 0:
            addend = -self
            other = -other
        else:
            addend = self.copy()

        result = Point(self.curve)
        # Iterate over all bits starting by the LSB

        while other:
            if other & 1:
                result += addend

            addend._double()
            other >>= 1

        if x1 is not None and x1 != result:
            raise ValueError('pizdos')

        return result

    def __str__(self):
        if self.inf:
            return 'Inf'

        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()


def make_keypair(curve):
    priv = random.randint(1, curve.field.n)
    pub = curve.g * priv
    return Keypair(curve, priv, pub)


class Keypair(object):
    def __init__(self, curve, priv=None, pub=None):
        if priv is None and pub is None:
            raise ValueError("Private and/or public key must be provided")
        self.curve = curve
        self.can_sign = True
        self.can_encrypt = True
        if priv is None:
            self.can_sign = False
        self.priv = priv
        self.pub = pub
        if pub is None:
            self.pub = self.curve.g * self.priv


class ECDH(object):
    def __init__(self, keypair):
        self.keypair = keypair

    def get_secret(self, keypair):
        if self.keypair.can_sign and keypair.can_encrypt:
            secret = keypair.pub * self.keypair.priv
        elif self.keypair.can_encrypt and keypair.can_sign:
            secret = self.keypair.pub * keypair.priv
        else:
            raise ValueError("Missing crypto material to generate DH secret")
        return secret


def lg(a, p):
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls


def sqrtp(a, p):
    a %= p
    if a == 0:
        return [0]

    if p == 2:
        return [a]

    if lg(a, p) != 1:
        return []

    if p % 4 == 3:
        x = pow(a, (p + 1) >> 2, p)
        return [x, p-x]

    q, s = p - 1, 0
    while q & 1 == 0:
        s += 1
        q >>= 1
    z = 1
    while lg(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    x = pow(a, (q + 1) >> 1, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        i, e = 0, 2
        for i in xrange(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        b = pow(c, 1 << (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]


def ec2osp(point, to_bytes=to_bytes):
    x = point.x
    y = point.y & 1
    compressed = y << point.curve.bits | x
    return to_bytes(compressed)


def osp2ec(curve, bytes, from_bytes=from_bytes):
    compressed = from_bytes(bytes)
    y = compressed >> curve.bits
    x = compressed & (1 << curve.bits) - 1
    if x == 0:
        y = curve.b
    else:
        result = sqrtp(x ** 3 + curve.a * x + curve.b, curve.field.p)
        if len(result) == 1:
            y = result[0]
        elif len(result) == 2:
            y1, y2 = result
            y = y1 if (y1 & 1 == y) else y2
        else:
            return None

    return Point(curve, x, y)


__all__ = (
    egcd, mod_inv, Curve, SubGroup, Point,
    make_keypair, Keypair, ECDH,
    to_bytes, from_bytes,
    ec2osp, osp2ec
)
