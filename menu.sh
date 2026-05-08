#!/bin/bash
echo "------------------------------------------"
echo "   PALINDROMIC PRIME EXPLORER MENU"
echo "------------------------------------------"
echo "1) Check the Belphegor Sequence (666)"
echo "2) Hunt for a Personalized Name Prime"
echo "3) View the Hall of Fame (Results)"
echo "4) Check Background Hunt Progress"
echo "5) Exit"
echo "------------------------------------------"
read -p "Choose an option [1-5]: " opt

case $opt in
  1) python src/explore.py ;;
  2) python src/name_hunter.py ;;
  3) cat README.md ;;
  4) tail -n 20 name_primes.txt ;;
  5) exit ;;
  *) echo "Invalid option";;
esac
