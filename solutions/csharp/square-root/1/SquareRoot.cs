public static class SquareRoot
{
    public static int Root(int number)
    {
        for (int i = 0; i <= number; i++){
            if (i * i == number) { return i; }
        }
        return 0; // This should never run
    }
}
