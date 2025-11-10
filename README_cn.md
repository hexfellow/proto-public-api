# proto-public-api

[English](README.md) | [中文](README_cn.md)

此仓库提供 hexfellow 绝大多数机器人的 API 协议。API使用 Websocket 协议，数据使用 Google Protobuf 编码。Websocket与Protobuf被广泛应用于全世界，拥有几乎所有语言的支持库。因此，您总是可以选择您喜欢的语言来使用本API。Google官方网站提供了包括不限于 Python, C++, Rust, C#, Go, Dart, Kotlin, Objective-C, Ruby 等语言的的 Tutorial/Reference Guide。如果您不清楚Protobuf的用法，请参考Google等教程。

Websocket已经被广泛应用于全世界的各个领域，此处不再赘述。但是需要注意，我们的连接上只允许发送 Binary 消息，Text 消息会被视为错误。所有机器人的消息都是类型 `APIUp`，所有发送给机器人的消息都是类型 `APIDown`。您应该先查看 `public_api_up.proto` 和 `public_api_down.proto` 来开始理解本API的通信方式。

如果没有特别说明，WebSocket 服务会运行在 8439 端口。

请注意，您需要设置 TCP_NODELAY 以及 TCP_QUICKACK，以得到最小延迟的效果。

## KCP 连接

> 此节为拓展阅读，如果您没有足够的知识储备，请使用 Websocket 连接。

为了避开 TCP 的各种麻烦的参数调整，进一步减小延迟以及抖动，增加了 KCP 连接选项。使用 KCP 前，必须使用 Websocket 连接进行握手。conv id 将等于 APIUp 中的 session id。

上下的 KCP Stream 都需要解包出 Protobuf 消息，然后进行处理。

<!-- TODO 包定义 -->

同时，参考了 https://github.com/skywind3000/kcp/wiki/Cooperate-With-Tcp-Server 的建议，如果 Websocket 连接断开，KCP 连接也会被认为断开。

握手大致流程：
1. 连接上 Websocket, 客户端从 WebSocket 获取 session id。然后发送 APIDown.EnableKcp 消息。EnableKcp 中 client_peer_port 填写 Client 所使用的 Socket 的端口。kcp_config 请使用注释中提供的默认值。
2. 等待 APIUp 中的 kcp_config 出现。从 kcp_config 中获取 KCP 连接端口。
3. 从KCP主动发送一条APIDown消息，来通知Server可以开始发送数据。
4. 更改 Websocket 的报告频率为 Rf1Hz。（可选但强烈建议，因为接下来Websocket连接意义不大了，仅用于保证KCP连接的存活）
5. 可以愉快的正常通信了。注意此时仍然可以从 Websocket 获取数据，并且 KCP 和 Websocket 将会有相同的 session id，意味着控制权是共享的。
