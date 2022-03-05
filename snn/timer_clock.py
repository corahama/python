class TimerClock:

    #Time in ms with delta_t=1
    def __init__(self, t_ini = 0, t_end = 1000, delta_t = 1) -> None:
        self.t_ini = t_ini
        self.t_end = t_end
        self.delta_t = delta_t
        self.t  = t_ini

    def timming(self) -> int:
        while self.t < self.t_end:
            yield self.t
            self.t += self.delta_t

    def get_t(self):
        return self.t
