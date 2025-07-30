def production_rate_per_hour:
  if . <= 4 then . * 221
  elif . <= 8 then . * 221 * 0.9
  elif . == 9 then . * 221 * 0.8
  else . * 221 * 0.77
  end
;

def working_items_per_minute:
  .
  | production_rate_per_hour
  | . / 60
  | floor
;



.speed | (production_rate_per_hour, working_items_per_minute)
