package com.pfsassistant_kotlin

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform