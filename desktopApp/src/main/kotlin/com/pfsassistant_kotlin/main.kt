package com.pfsassistant_kotlin

import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application

fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "PFSAssistant-Kotlin",
    ) {
        App()
    }
}