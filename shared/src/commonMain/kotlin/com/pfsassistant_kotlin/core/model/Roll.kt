package com.pfsassistant_kotlin.core.model


data class Roll(
    val total: Int,
    val natMin: Boolean = false,
    val natMax: Boolean = false
) {
    companion object {
        /**
         * Creates a Roll from a primary set of dice (which determines natMin/natMax)
         * an optional list of additional dice, and a modifier.
         *
         * @param modifier Flat bonus added to the total.
         * @param primaryDiceCount Number of primary dice (default 1).
         * @param primaryDiceSize Size of the primary dice (default 20).
         * @param additionalDice List of extra dice to roll, represented as Pairs of (count, size).
         * @param rollProvider Function that takes a dice size and returns a rolled value.
         */
        fun fromDice(
            modifier: Int,
            primaryDiceCount: Int = 1,
            primaryDiceSize: Int = 20,
            additionalDice: List<Pair<Int, Int>> = emptyList(),
            rollProvider: (Int) -> Int = { size -> (1..size).random() }
        ): Roll {
            var total = modifier
            var allMax = true
            var allMin = true

            repeat(primaryDiceCount) {
                val roll = rollProvider(primaryDiceSize)
                total += roll
                if (roll != primaryDiceSize) allMax = false
                if (roll != 1) allMin = false
            }

            for ((count, size) in additionalDice) {
                repeat(count) {
                    total += rollProvider(size)
                }
            }

            return Roll(
                total = total,
                natMax = primaryDiceCount == 1 && allMax,
                natMin = primaryDiceCount == 1 && allMin
            )
        }
    }
}