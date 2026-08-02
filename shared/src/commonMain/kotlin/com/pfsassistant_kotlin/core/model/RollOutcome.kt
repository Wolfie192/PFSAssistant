package com.pfsassistant_kotlin.core.model


fun Roll.getOutcome(dc: Int): CheckOutcome {
    val diff = total - dc
    var outcome = when {
        diff >= 10 -> CheckOutcome.CRIT_SUCCESS
        diff >= 0 -> CheckOutcome.SUCCESS
        diff <= -10 -> CheckOutcome.CRIT_FAIL
        else -> CheckOutcome.FAIL
    }

    if (natMax){
        outcome = upgradeOutcome(outcome)
    }
    if (natMin) {
        outcome = downgradeOutcome(outcome)
    }

    return outcome
}

private fun upgradeOutcome(current: CheckOutcome): CheckOutcome = when (current) {
    CheckOutcome.CRIT_FAIL -> CheckOutcome.FAIL
    CheckOutcome.FAIL -> CheckOutcome.SUCCESS
    CheckOutcome.SUCCESS, CheckOutcome.CRIT_SUCCESS -> CheckOutcome.CRIT_SUCCESS
}

private fun downgradeOutcome(current: CheckOutcome): CheckOutcome = when (current) {
    CheckOutcome.CRIT_SUCCESS -> CheckOutcome.SUCCESS
    CheckOutcome.SUCCESS -> CheckOutcome.FAIL
    CheckOutcome.FAIL, CheckOutcome.CRIT_FAIL -> CheckOutcome.CRIT_FAIL
}