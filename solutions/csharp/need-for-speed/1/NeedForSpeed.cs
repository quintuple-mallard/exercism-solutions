class RemoteControlCar
{
    private int _speed;
    private int _drain;
    private int _battery;
    private int _distance;
    public RemoteControlCar(int speed, int drain) {
        this._speed = speed;
        this._drain = drain;
        this._battery = 100;
        this._distance = 0;
    }

    public bool BatteryDrained()
    {
        return this._battery < this._drain;
    }

    public int DistanceDriven()
    {
        return this._distance;
    }

    public void Drive()
    {
        if (!this.BatteryDrained()) {
            this._distance += this._speed;
            this._battery -= this._drain;
        }
    }

    public static RemoteControlCar Nitro()
    {
        return new RemoteControlCar(50, 4);
    }
}

class RaceTrack
{
    private int _distance;
    public RaceTrack(int distance) {
        this._distance = distance;
    }

    public bool TryFinishTrack(RemoteControlCar car)
    {
        while (!car.BatteryDrained()) {
            car.Drive();
            if (car.DistanceDriven() >= this._distance) {
                return true;
            }
        }
        return false;
    }
}
