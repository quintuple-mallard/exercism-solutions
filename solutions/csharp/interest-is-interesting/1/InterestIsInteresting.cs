static class SavingsAccount
{
    public static float InterestRate(decimal balance)
    {
        if (balance < 0) {
            return 3.213f;
        } else if (balance < 1000) {
            return 0.5f;
        } else if (balance < 5000) {
            return 1.621f;
        } else {
            return 2.475f;
        }
    }

    public static decimal Interest(decimal balance)
    {
        return balance * Convert.ToDecimal(SavingsAccount.InterestRate(balance) / 100);
    }

    public static decimal AnnualBalanceUpdate(decimal balance)
    {
        return balance + SavingsAccount.Interest(balance);
    }

    public static int YearsBeforeDesiredBalance(decimal balance, decimal targetBalance)
    {
        int years = 0;
        while (balance <= targetBalance) {
            years++;
            balance = SavingsAccount.AnnualBalanceUpdate(balance);
        }
        return years;
    }
}
