local Robot = {}
local RIGHT = {
  north = "east",
  east = "south",
  south = "west",
  west = "north"
}
local OFFSETS = {
  north = {x = 0, y = 1},
  east = {x = 1, y = 0},
  south = {x = 0, y = -1},
  west = {x = -1, y = 0}
}
function Robot:advance()
  local offset = OFFSETS[Robot.heading]
  Robot.x, Robot.y = Robot.x + offset.x, Robot.y + offset.y
end
function Robot:turn_right()
  Robot.heading = RIGHT[Robot.heading]
end
function Robot:move_single(instruction) 
  if instruction == "A" then
    Robot:advance()
  elseif instruction == "R" then
    Robot:turn_right()
  elseif instruction == "L" then
    Robot:turn_right()
    Robot:turn_right()
    Robot:turn_right()
  else
    error("invalid instruction")
  end
end

function Robot:move(instruction)
  for char in instruction:gmatch"." do
    Robot:move_single(char)
  end
end
return function(config)
  Robot.x, Robot.y, Robot.heading = config.x, config.y, config.heading
  return Robot
end
