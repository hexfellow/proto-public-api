# 1.3
- Added new robot type: RtPureForwardOnlyV2
- Added HexCanApixxx messages for CAN forwarding.

# 1.4
- Change HexCanApiCanAnyFrame to HexCanApiCanAnyFrames.
- Add HcanInvalid for HexCanApiCanBusNumber.
- Change MitMotorTarget's position unit to rad.

# 1.5
- Added protocol_major_version and protocol_minor_version to api down.
- Added RtMaverX4H1 & RtMaverL4H1 & RtArmArcherX7h1.
- Added SecondaryDeviceType SdtHandGr100.
- Added SpeedWithMaxCurrent & pos_with_trapezoidal_velocity for SingleMotorTarget.
- Added new PosVelAccTarget message (position / velocity / acceleration in rad · rad·s⁻¹ · rad·s⁻²).
- Added ArmApiCompensatedJointPositionCommand for ArmApiControlCommand.
- Change FollowMotorTarget's position unit to rad (reserved old encoder field 3).
- Change ArmApiJointPositionCommand: replaced repeated double joint_positions (field 1, reserved) with repeated PosVelAccTarget joint_targets (field 2).