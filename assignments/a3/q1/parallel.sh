counter=0
while [ $counter -le 4 ]
do
   
    taskset -c $counter python ./genetic_algorithm.py $counter &
    echo $counter
    counter=$(( $counter + 1 ))

done