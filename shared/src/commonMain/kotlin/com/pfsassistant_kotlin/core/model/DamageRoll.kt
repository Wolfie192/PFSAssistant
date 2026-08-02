package com.pfsassistant_kotlin.core.model

data class DamageRoll(
    val total: Int,
    val damageType: DamageType
) {
    companion object {
        /**
         * Creates a DamageRoll by rolling a specific number of dice and adding a modifier.
         *
         * @param diceCount Number of dice
         * @param diceSize Size of the damage dice.
         * @param modifier Flat bonus added to the damage total.
         * @param damageType The type of damage dealt.
         * @param rollProvider Function that takes the size and returns a rolled value.
         */
        fun fromDice(
            diceCount: Int,
            diceSize: Int,
            modifier: Int,
            damageType: DamageType,
            rollProvider: (Int) -> Int = { size -> (1..size).random() }
        ): DamageRoll {
            var total = modifier

            repeat(diceCount) {
                val roll = rollProvider(diceSize)
                total += roll
            }


            return DamageRoll(
                total = total,
                damageType = damageType
            )
        }
    }
}
