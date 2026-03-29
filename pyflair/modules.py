import os


class FlairMath:
    @staticmethod
    def rpm(rate, seconds) -> int:
        return int(rate / seconds * 60)

    @staticmethod
    def rps(rate, seconds) -> int:
        return int(rate / seconds)

    @staticmethod
    def rph(rate, seconds) -> int:
        return int(rate / seconds * 3600)

    @staticmethod
    def rpd(rate, seconds) -> int:
        return int(rate / seconds * 86400)

    @staticmethod
    def rpy(rate, seconds) -> int:
        return int(rate / seconds * 31536000)

    @staticmethod
    def estimate(total: int, done: int, valid: int) -> int:
        return round(valid / done * total)

    @staticmethod
    def percent(total: int, done: int) -> float:
        return round(done / total * 100, 2)


class FlairTools:
    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')