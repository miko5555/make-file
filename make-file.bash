#!/bin/bash
	   
        for (( c=1; c<=$1; c++ ))
	do 
	touch $2.$c

#echo "#!$3" >> $2.$c 
# չեմ ուզում 3֊րդ արգումենտ լինի, փորձում եմ սքրիպտն իրանով տպի

echo "#!" >> $2.$c
which bash >> $2.$c 

#'which bash'=A
#echo "#! $A" >> $2.$c
	done
