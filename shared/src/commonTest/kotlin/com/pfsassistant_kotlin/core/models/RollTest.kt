package com.pfsassistant_kotlin.core.models

import com.pfsassistant_kotlin.core.model.Roll
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class RollTest {

    @Test
    fun roll_initialization() {
        val roll = Roll(total = 25, natMax = false, natMin = false)

        assertEquals(25, roll.total)
        assertFalse(roll.natMax)
        assertFalse(roll.natMin)

        val rollMax = Roll(total = 25, natMax = true, natMin = false)

        assertEquals(25, rollMax.total)
        assertTrue(rollMax.natMax)
        assertFalse(rollMax.natMin)

        val rollMin = Roll(total = 25, natMax = false, natMin = true)

        assertEquals(25, rollMin.total)
        assertFalse(rollMin.natMax)
        assertTrue(rollMin.natMin)
    }

    @Test
    fun roll_from_modifier() {
        val roll = Roll.fromDice(modifier = 7) { 15 }

        assertEquals(22, roll.total)
        assertFalse(roll.natMax)
        assertFalse(roll.natMin)

        val rollMax = Roll.fromDice(modifier = 7) { 20 }

        assertEquals(27, rollMax.total)
        assertTrue(rollMax.natMax)
        assertFalse(rollMax.natMin)

        val rollMin = Roll.fromDice(modifier = 7) { 1 }

        assertEquals(8, rollMin.total)
        assertFalse(rollMin.natMax)
        assertTrue(rollMin.natMin)
    }

    @Test
    fun roll_from_dice_with_additional_dice() {
        val roll = Roll.fromDice(modifier = 7, additionalDice = listOf(Pair(1, 6)),
            rollProvider = { diceSize ->
                when (diceSize) {
                    20 -> 15
                    6 -> 4
                    else -> throw IllegalArgumentException("unexpected dice size")
                }
            }
        )

        assertEquals(26, roll.total)
        assertFalse(roll.natMax)
        assertFalse(roll.natMin)

        val rollMax = Roll.fromDice(modifier = 7, additionalDice = listOf(Pair(1, 6)),
            rollProvider = { diceSize ->
                when (diceSize) {
                    20 -> 20
                    6 -> 4
                    else -> throw IllegalArgumentException("unexpected dice size")
                }
            }
        )

        assertEquals(31, rollMax.total)
        assertTrue(rollMax.natMax)
        assertFalse(rollMax.natMin)

        val rollMin = Roll.fromDice(modifier = 7, additionalDice = listOf(Pair(1, 6)),
            rollProvider = { diceSize ->
                when (diceSize) {
                    20 -> 1
                    6 -> 4
                    else -> throw IllegalArgumentException("unexpected dice size")
                }
            }
        )

        assertEquals(12, rollMin.total)
        assertFalse(rollMin.natMax)
        assertTrue(rollMin.natMin)
    }
}