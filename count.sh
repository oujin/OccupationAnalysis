awk '{gsub(/[\[\]]/,"",$24);split($24,arr,",");for(i in arr){print(arr[i]);}}' \
positions.txt | sort | \
awk '{cnt[$0]++}END{for(w in cnt)printf("%s %d\n",w,cnt[w])|"sort -r -n -k2"}'

