class BirdCount
{
    private int[] birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        return new [] {0, 2, 5, 3, 7, 8, 4};
    }

    public int Today()
    {
        return this.birdsPerDay[birdsPerDay.Length - 1];
    }

    public void IncrementTodaysCount()
    {
        this.birdsPerDay[birdsPerDay.Length - 1]++;
    }

    public bool HasDayWithoutBirds()
    {
        return Array.Exists(this.birdsPerDay, count => count == 0);
    }

    public int CountForFirstDays(int numberOfDays)
    {
        int sum = 0;
        for (int i = 0; i < numberOfDays; i++) {
            sum += this.birdsPerDay[i];
        }
        return sum;
    }

    public int BusyDays()
    {
        int busyCount = 0;
        foreach (int count in this.birdsPerDay) {
            if (count >= 5) {
                busyCount++;
            }
        }
        return busyCount;
    }
}
