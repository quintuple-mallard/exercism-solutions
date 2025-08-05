abstract class Character
{
    protected string type;
    protected Character(string characterType)
    {
        this.type = characterType;
    }

    public abstract int DamagePoints(Character target);

    public virtual bool Vulnerable()
    {
        return false;
    }

    public override string ToString()
    {
        return $"Character is a {this.type}";
    }
}

class Warrior : Character
{
    public Warrior() : base("Warrior")
    {
    }

    public override int DamagePoints(Character target)
    {
        return target.Vulnerable() ? 10 : 6;
    }
}

class Wizard : Character
{
    private bool hasSpell;
    public Wizard() : base("Wizard")
    {
    }

    public override int DamagePoints(Character target)
    {
        return this.hasSpell ? 12 : 3;
    }

    public void PrepareSpell()
    {
        this.hasSpell = true;
    }
    public override bool Vulnerable() {
        return !this.hasSpell;
    }
}
