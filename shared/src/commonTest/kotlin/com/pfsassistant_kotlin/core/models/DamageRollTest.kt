package com.pfsassistant_kotlin.core.models

import com.pfsassistant_kotlin.core.model.DamageRoll
import com.pfsassistant_kotlin.core.model.DamageType
import kotlin.test.Test
import kotlin.test.assertEquals

class DamageRollTest {

    @Test
    fun damage_roll_initialization_and_property_test() {
        val roll = DamageRoll(total = 17, damageType = DamageType.BLUDGEONING)

        assertEquals(17, roll.total)
        assertEquals(DamageType.BLUDGEONING, roll.damageType)
    }

    @Test
    fun damage_roll_from_dice() {
        val roll = DamageRoll.fromDice(2, 6, 4, DamageType.BLUDGEONING, rollProvider = { 4 })

        assertEquals(12, roll.total)
        assertEquals(DamageType.BLUDGEONING, roll.damageType)
    }
}