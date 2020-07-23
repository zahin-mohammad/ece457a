counter=0
while [ $counter -le 7 ]
do
   
    taskset -c $counter python ./ant_colony.py $counter &
    echo $counter
    counter=$(( $counter + 1 ))

done