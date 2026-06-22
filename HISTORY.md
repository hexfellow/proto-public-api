# Change Log

## Rules
- Adding new messages/enum without rolling a new version is allowed, if expected to work anyway.
- Any change to current field should requires a new version, and generally not recommended.

## 1.3
- Added new robot type: RtPureForwardOnlyV2
- Added HexCanApixxx messages for CAN forwarding.

## 1.4
- Change HexCanApiCanAnyFrame to HexCanApiCanAnyFrames.
- Add HcanInvalid for HexCanApiCanBusNumber.
- Change MitMotorTarget's position unit to rad.

## 1.5
- Added protocol_major_version and protocol_minor_version to api down.
- Added RtMaverX4H1 & RtMaverL4H1 & RtArmArcherX7h1.
- Added SecondaryDeviceType SdtHandGr100.
- Added SpeedWithMaxCurrent & pos_with_trapezoidal_velocity for SingleMotorTarget.
- Added new PosVelAccTarget message (position / velocity / acceleration in rad · rad·s⁻¹ · rad·s⁻²).
- Added ArmApiCompensatedJointPositionCommand for ArmApiControlCommand.
- Change FollowMotorTarget's position unit to rad (reserved old encoder field 3).
- Change ArmApiJointPositionCommand: replaced repeated double joint_positions (field 1, reserved) with repeated PosVelAccTarget joint_targets (field 2).
- Added BoardcastMessage, BmHardwareMessage, BmRobotMessage.

## 2.0
- Removed LinearLiftStatus and RotateLiftStatus. Treat them as Arms.
- Added RobotMode and OvertakenReason.
- Move session holder to APIUp.
### New messages
- MotionTarget (renamed from PosVelAccTarget): position / velocity / acceleration / torque (rad|m, rad/s|m/s, rad/s²|m/s², Nm), all optional. Added torque field.
- SpeedWithMaxCurrent: speed (rad/s) with max_current limit (A).
- PosVelTorqueTarget: position / velocity / torque (rad, rad/s, Nm). Replaces FollowMotorTarget.
### SingleMotorTarget
- Added SpeedWithMaxCurrent and pos_with_trapezoidal_velocity (PosVelAccTarget).
- Changed FollowMotorTarget follow_motor_target to PosVelAccTarget follow_motor_target.
### ArmStatus
- Added optional Pose end_pose. For non-standard arm types, there may be no pose information.
### HandCommand
- Changed to oneof, supporting three control modes:
  - `motor_targets` (MotorTargets)
  - `tau_with_speed_limit` (PosVelAccTarget) — torque control with speed limit
  - `pos_with_speed_and_torque_limit` (PosVelTorqueTarget) — position control with speed and torque limits
### ArmApiJointPositionCommand
- Changed repeated double joint_positions (field 1, reserved) to repeated PosVelAccTarget joint_motion_params (field 2).
- Merged ArmApiCompensatedJointPositionCommand: added optional AccelerationSource acceleration_source (field 3).
### ArmApiEndEffectorCommand
- Added repeated PosVelAccTarget joint_motion_params (field 3) for per-joint motion planning.
### ArmCommand
- Reserved field 6.
- Removed arm_api_compensated_joint_position_command (merged into ArmApiJointPositionCommand).
### APIDown
- Added EnterStandbyMode. Only works when robot is in RmStandby or RmRunning mode.
