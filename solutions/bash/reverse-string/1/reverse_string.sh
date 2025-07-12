#!/usr/bin/env bash

main() {
  backward=''
  for (( i=0; i<${#1}; i++ )); do
    backward="${1:i:1}$backward"
  done
  echo "$backward"
}
main "$@"
