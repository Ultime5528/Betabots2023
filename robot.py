#!/usr/bin/env python3
import math
from typing import Optional

import commands2.button
import wpilib

from commands.drive import Drive
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        wpilib.LiveWindow.enableAllTelemetry()
        wpilib.LiveWindow.setEnabled(True)
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)

        self.xboxremote = commands2.button.CommandXboxController(0)

        self.drivetrain = Drivetrain(lambda: self.getPeriod())

        self.drivetrain.setDefaultCommand(
            Drive(self.drivetrain, self.xboxremote)
        )


if __name__ == "__main__":
    wpilib.run(Robot)
