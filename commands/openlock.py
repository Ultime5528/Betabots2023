from utils.safecommand import SafeCommand
from subsystems.blocker import Blocker


class OpenLock(SafeCommand):
    def __init__(self, blocker: Blocker):
        super().__init__()
        self.blocker = blocker
        self.addRequirements(self.blocker)

    def execute(self) -> None:
        if not self.blocker.limit_switch_blocker.get():
            self.blocker.unlock()
