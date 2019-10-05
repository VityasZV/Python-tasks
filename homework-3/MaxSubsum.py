def MaxSubsum():
    k = int(input())
    max_subsum = []
    all_subsum = []
    while (k):
        #max_subsum.append(k)
        for j in range(len(all_subsum)):
            all_subsum[j]+=k
            if all_subsum[j] > max_subsum[j] :
                max_subsum[j] = all_subsum[j]
        all_subsum.append(k)
        max_subsum.append(k)
        k = int(input())
    print(max(max_subsum))

MaxSubsum()
