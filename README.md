# proto-public-api

[English](README.md) | [中文](README_cn.md)

This repository provides the API protocol for most Hexfellow bots. The API uses the WebSocket protocol, with data encoded using Google Protobuf. WebSocket and Protobuf are widely used globally and have support libraries for almost every language. Therefore, you can always choose your preferred language to use this API. Google's official website offers tutorials/reference guides for languages including, but not limited to, Python, C++, Rust, C#, Go, Dart, Kotlin, Objective-C, and Ruby. If you are unsure how to use Protobuf, please refer to tutorials from Google and others.

WebSocket is widely used across various fields worldwide, so it won't be elaborated on here. However, note that our connection only allows sending Binary messages; Text messages will be considered errors. All messages from the bots are of type `APIUp`, and all messages sent to the bots are of type `APIDown`. You should first review `public_api_up.proto` and `public_api_down.proto` to start understanding the communication method of this API.

Unless otherwise specified, the WebSocket service runs on port 8439.
