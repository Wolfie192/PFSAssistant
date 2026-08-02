package com.pfsassistant_kotlin.core.models

import com.pfsassistant_kotlin.core.model.CheckOutcome
import com.pfsassistant_kotlin.core.model.Roll
import com.pfsassistant_kotlin.core.model.getOutcome
import kotlin.test.Test
import kotlin.test.assertEquals

class RollOutcomeTest {

    @Test
    fun roll_outcome_test() {
        val roll = Roll(total = 20, natMax = false, natMin = false)

        assertEquals(CheckOutcome.SUCCESS, roll.getOutcome(20))

        val rollMax = Roll(total = 20, natMax = true,  natMin = false)

        assertEquals(CheckOutcome.CRIT_SUCCESS, rollMax.getOutcome(20))

        val rollMin = Roll(total = 20, natMax = false, natMin = true)

        assertEquals(CheckOutcome.FAIL, rollMin.getOutcome(20))
    }
}