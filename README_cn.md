# proto-public-api

[English](README.md) | [中文](README_cn.md)

此仓库提供 hexfellow 绝大多数机器人的 API 协议。API使用 Websocket 协议，数据使用 Google Protobuf 编码。Websocket与Protobuf被广泛应用于全世界，拥有几乎所有语言的支持库。因此，您总是可以选择您喜欢的语言来使用本API。Google官方网站提供了包括不限于 Python, C++, Rust, C#, Go, Dart, Kotlin, Objective-C, Ruby 等语言的的 Tutorial/Reference Guide。如果您不清楚Protobuf的用法，请参考Google等教程。

Websocket已经被广泛应用于全世界的各个领域，此处不再赘述。但是需要注意，我们的连接上只允许发送 Binary 消息，Text 消息会被视为错误。所有机器人的消息都是类型 `APIUp`，所有发送给机器人的消息都是类型 `APIDown`。您应该先查看 `public_api_up.proto` 和 `public_api_down.proto` 来开始理解本API的通信方式。

如果没有特别说明，WebSocket 服务会运行在 8439 端口。
