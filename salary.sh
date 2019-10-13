awk '{cnt[$9]++}END{for(w in cnt)printf("%s %d\n",w,cnt[w])}' \
positions.txt | sort -rn -k2