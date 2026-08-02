package com.pfsassistant_kotlin.core.model

enum class CheckOutcome(val displayName: String) {
    CRIT_SUCCESS("Critical Success"),
    SUCCESS("Success"),
    FAIL("Failure"),
    CRIT_FAIL("Critical Failure")
}