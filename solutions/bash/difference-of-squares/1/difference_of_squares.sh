#!/usr/bin/env bash
square_of_sum() {
  sum=0
  for (( i=0;i<=$1;i++ )) do
    sum=$((sum + i))
  done
  echo $((sum**2))
}
sum_of_squares() {
  sum=0
  for (( i=0;i<=$1;i++ )) do
    sum=$((sum + (i**2)))
  done
  echo $sum
}
if [ "$1" = "square_of_sum" ]
then
  result=$(square_of_sum $2)
  echo "$result"
elif [ "$1" = "sum_of_squares" ]
then
  result=$(sum_of_squares $2)
  echo "$result"
else
  sum_of_squares_result=$(sum_of_squares $2)
  square_of_sum_result=$(square_of_sum $2)
  echo $((square_of_sum_result - sum_of_squares_result))
fi