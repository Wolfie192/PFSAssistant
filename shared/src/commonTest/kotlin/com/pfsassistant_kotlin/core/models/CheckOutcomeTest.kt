package com.pfsassistant_kotlin.core.models

import com.pfsassistant_kotlin.core.model.CheckOutcome
import kotlin.test.Test
import kotlin.test.assertEquals

class CheckOutcomeTest {

    @Test
    fun check_outcome_display_names() {
        assertEquals("Critical Success", CheckOutcome.CRIT_SUCCESS.displayName)
        assertEquals("Success", CheckOutcome.SUCCESS.displayName)
        assertEquals("Failure", CheckOutcome.FAIL.displayName)
        assertEquals("Critical Failure", CheckOutcome.CRIT_FAIL.displayName)
    }
}