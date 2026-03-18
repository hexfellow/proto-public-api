# 1.3
- Added new robot type: RtPureForwardOnlyV2
- Added HexCanApixxx messages for CAN forwarding.


# 2.0
- Removed LinearLiftStatus and RotateLiftStatus. Treat them as Arms.
- Added RobotMode and OvertakenReason.
- Move session holder to APIUp.
- No longer checks kcp peer. KCP messages can now be sent from any IP and port, as long as conv id is valid.
