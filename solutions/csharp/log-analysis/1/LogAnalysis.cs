public static class LogAnalysis 
{
    public static string SubstringAfter(this string str, string delim) {
        return str.Split(delim)[1];
    }

    public static string SubstringBetween(this string str, string delimStart, string delimEnd) {
        return str.Split(delimStart)[1].Split(delimEnd)[0];
    }
    
    public static string Message(this string str) {
        return str.Split(": ")[1];
    }
    public static string LogLevel(this string str) {
        return str.Split(": ")[0].SubstringBetween("[", "]");
    }
}