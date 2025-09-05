defmodule KitchenCalculator do
  def get_volume(volume_pair), do: elem(volume_pair, 1)

  def to_milliliter({:milliliter, vol}), do: {:milliliter, vol}
  def to_milliliter({:cup, vol}), do: {:milliliter, vol * 240}
  def to_milliliter({:fluid_ounce, vol}), do: {:milliliter, vol * 30}
  def to_milliliter({:teaspoon, vol}), do: {:milliliter, vol * 5}
  def to_milliliter({:tablespoon, vol}), do: {:milliliter, vol * 15}


  def from_milliliter({:milliliter, vol}, :milliliter = unit), do: {unit, vol}
  def from_milliliter({:milliliter, vol}, :cup = unit), do: {unit, vol / 240}
  def from_milliliter({:milliliter, vol}, :fluid_ounce = unit), do: {unit, vol / 30}
  def from_milliliter({:milliliter, vol}, :teaspoon = unit), do: {unit, vol / 5}
  def from_milliliter({:milliliter, vol}, :tablespoon = unit), do: {unit, vol / 15}

  def convert(volume_pair, unit), do: from_milliliter(to_milliliter(volume_pair), unit)
end
