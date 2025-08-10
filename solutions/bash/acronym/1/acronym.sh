#!/usr/bin/env bash
cleaned="${1//[^a-zA-Z -]/}"
cleaned="${cleaned//-/ }"
acronym=""
for word in $cleaned; do
  acronym+="${word:0:1}"
done
echo "${acronym^^}"