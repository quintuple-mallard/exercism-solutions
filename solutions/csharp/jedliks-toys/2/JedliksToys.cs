class RemoteControlCar
{
    private int _distance;
    private int _battery = 100;
    public static RemoteControlCar Buy() => new RemoteControlCar();

    public string DistanceDisplay() => $"Driven {this._distance} meters";

    public string BatteryDisplay()
    {
        if (this._battery == 0) {
            return "Battery empty";
        }
        return $"Battery at {this._battery}%";
    }

    public void Drive()
    {
        if (this._battery == 0) {
            return;
        }
        this._battery--;
        this._distance += 20;
    }
}
