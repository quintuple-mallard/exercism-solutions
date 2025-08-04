static class Badge
{
    public static string Print(int? id, string name, string? department)
    {
        string idStr = "";
        if (id != null) {
            idStr = $"[{id}] - ";
        }
        if (department == null) {
            department = "OWNER";
        }
        return $"{idStr}{name} - {department.ToUpper()}";
    }
}
