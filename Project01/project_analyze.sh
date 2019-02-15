#!/bin/bash

MergeLog ()
{
	rm -f "merge.log"
	log=`git log --oneline`
	while read -r line; do
    		if [[ ! -z `echo $line | grep "Merge"` ]]; then
			hash=`echo $line | cut -d " " -f 1`
			echo $hash >> merge.log
			echo "Found: $hash"
		fi
	done <<< $log
	echo "Done!"
}

main ()
{
	while true; do
		clear
		echo "Please select a job to do:"
		echo "    1.Merge Log"
		echo "    2.Exit"
		read -p "Enter the number index > " idx
	        case $idx in
	        	[1]) MergeLog;;
			[2]) exit;;
        		* ) echo -e "\nPlease enter a selection.\n";;
        	esac
		read -rsn1 -p "Press any key to continue...";
	done
}

main;
