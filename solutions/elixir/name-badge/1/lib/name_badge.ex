defmodule NameBadge do
  def print(id, name, department) do
    id_block = if id, do: "[#{id}] - ", else: ""
    
    department = if department, do: department, else: "owner"
    
    "#{id_block}#{name} - #{String.upcase(department)}"
  end
end
