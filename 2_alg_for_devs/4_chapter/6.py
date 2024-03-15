class State:
    def __init__(self, a, b, st) -> None:
        self.a = a
        self.b = b
        self.st = st


def power2(a: int, b: int) -> int:
    st = []
    st.append(State(a, b, 0))
    ret = 0

    while st:
        a = st[-1].a
        b = st[-1].b
        pos = st[-1].st
        st.pop()

        if pos == 0:
            if b == 0:
                ret = 0
                continue
            if b % 2 == 0:
                st.append(State(a, b, 1))
                st.append(State(a, b // 2, 0))
            else:
                st.append(State(a, b, 2))
                st.append(State(a, b - 1, 0))
            continue

        elif pos == 1:
            ret = ret * ret
            continue
        else:
            ret = ret * a
            continue

    return ret


if __name__ == "__main__":
    print(power2(2, 3))
