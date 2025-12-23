module MariosMarvellousLasagna exposing (remainingTimeInMinutes)


preparationTimeInMinutes layers = 
  let 
    minutesPerLayer = 2
  in 
    minutesPerLayer * layers

remainingTimeInMinutes layers minutes =
  let 
    expectedMinutesInOven = 40
    ovenTime = expectedMinutesInOven - minutes
    layerTime = preparationTimeInMinutes layers
  in 
    ovenTime + layerTime