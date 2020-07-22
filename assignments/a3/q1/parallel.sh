counter=0
while [ $counter -le 4 ]
do
   
    # your_command_string=""
    # output=$(eval "$your_command_string")
    taskset -c $counter python ./genetic_algorithm.py $counter &
    echo $counter
    echo "$output"
    counter=$(( $counter + 1 ))

done