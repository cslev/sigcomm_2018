#!/bin/bash

function print_help
{
  echo -e "This script generates all favicons by converting your desired image (set as first argument)"
  echo -e "package imagemagick needs to be installed!"
  echo -e "Usage: ./create_favicons.sh <original_icon>"
  exit
}

if [ $# -lt 1 ]
then
  echo -e "${red}Not enough parameters${none}"
  print_help
  exit
fi


favicon=$1

convert -resize 48x48 $favicon favicon.ico
convert -resize 32x32 $favicon favicon-32x32.png
convert -resize 16x16 $favicon favicon-16x16.png
convert -resize 150x150 $favicon mstile-150x150.png
convert -resize 180x180 $favicon apple-touch-icon.png
convert -resize 512x512 $favicon android-chrome-512x512.png
convert -resize 192x192 $favicon android-chrome-192x192.png

