import commands2.button
from wpimath.filter import SlewRateLimiter

from subsystems.drivetrain import Drivetrain
from utils.safecommand import SafeCommand


class Drive(SafeCommand):
    def __init__(
        self,
        drivetrain: Drivetrain,
        xbox_remote: commands2.button.CommandXboxController,
    ):
        super().__init__()
        self.addRequirements(drivetrain)
        self.xbox_remote = xbox_remote
        self.drivetrain = drivetrain

        self.m_xspeedLimiter = SlewRateLimiter(3)
        self.m_yspeedLimiter = SlewRateLimiter(3)
        self.m_rotLimiter = SlewRateLimiter(3)

    def execute(self):
        x_speed = (
            self.m_xspeedLimiter.calculate(self.xbox_remote.getLeftY())
            * -1
        )
        y_speed = (
            self.m_yspeedLimiter.calculate(self.xbox_remote.getLeftX())
            * -1
        )
        # TODO print joystick to see whats up with not being able to turn both ways
        rot = (
            self.m_rotLimiter.calculate(self.xbox_remote.getRightX())
            * -1
        )
        
        self.drivetrain.drive(x_speed, y_speed, rot, True, True)

    def end(self, interrupted: bool) -> None:
        self.drivetrain.drive(0.0, 0.0, 0.0, True, True)
