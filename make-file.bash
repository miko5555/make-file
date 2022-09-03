#!/bin/bash
	 
    
        for (( c=1; c<=$1; c++ ))
	do 
	touch $2.$c
echo "#!/usr/bin/bash" >> $2.$c
	done
