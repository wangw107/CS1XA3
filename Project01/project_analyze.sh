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
	echo "Please check "merge.log" under the same directory."
}

FileTypeCount ()
{
	declare -A extNames=(
		[".html"]="HTML"
		[".js"]="JavaScript"
		[".css"]="CSS"
		[".py"]="PythonScript"
		[".hs"]="HaskellScript"
		[".sh"]="ShellScript"
	)
	declare -A extCounts=(
		[".html"]=0
		[".js"]=0
		[".css"]=0
		[".py"]=0
		[".hs"]=0
		[".sh"]=0
	)
	files=`find .`
	while read -r file; do
		for ext in "${!extNames[@]}"; do
			if [[ $file == *$ext ]]; then
				extCounts[$ext]=$((extCounts[$ext]+1))
			fi
		done
	done <<< $files
	echo "Done!"
	for ext in "${!extNames[@]}"; do
		echo "${extNames[$ext]}: ${extCounts[$ext]}"
	done
}

DeleteUntrackedTemps ()
{
	untracked=`git ls-files . –exclude-standard –others`
        while read -r file; do
		if [[ $file == *".tmp" ]]; then
			echo "Removed ${file}"
			rm -f $file
		fi
	done <<< $untracked
	echo "Done!"
}

main ()
{
	while true; do
		clear
		echo "Please select a job to do:"
		echo "    1.Merge log"
		echo "    2.File type Count"
		echo "    3.Delete untracked *.tmp files"
		echo "    4.Exit"
		read -p "Enter the number index > " idx
	        case $idx in
	        	[1]) MergeLog;;
			[2]) FileTypeCount;;
			[3]) DeleteUntrackedTemps;;
			[4]) exit;;
        		* ) echo -e "\nPlease enter a selection.\n";;
        	esac
		read -rsn1 -p "Press any key to continue...";
	done
}

main;
