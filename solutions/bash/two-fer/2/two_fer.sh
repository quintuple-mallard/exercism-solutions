#!/usr/bin/env bash

if (( $# < 1 )); then
  echo "One for you, one for me."
else
  echo "One for $1, one for me."
fi