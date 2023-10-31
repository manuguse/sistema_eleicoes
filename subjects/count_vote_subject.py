from subjects import subject


class CountVoteSubject(subject.Subject):
    def __init__(self) -> None:
        self.__cadidate: str = ''
        self.__amount: int = 0

    def notify(self) -> None:
        for callback in super().get_observers():
            callback()

    def handle_events(self) -> None:
        self.notify()
