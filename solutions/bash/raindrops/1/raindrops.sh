#!/usr/bin/env bash
sound=""
if [ $(( $1 % 7)) -eq 0 ]; then
  sound="Plong$sound"
fi
if [ $(( $1 % 5)) -eq 0 ]; then
  sound="Plang$sound"
fi
if [ $(( $1 % 3)) -eq 0 ]; then
  sound="Pling$sound"
fi
if [ "$sound" = "" ]; then
  sound=$1
fi
echo $sound