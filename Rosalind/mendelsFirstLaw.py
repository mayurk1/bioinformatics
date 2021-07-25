def probability(k, m, n):
    sum = k + m + n
    # Probability of having at least one
    # dominant allele is = 
    # 1 - P(# recessive alleles)

    rr = (n/sum) * ((n-1)/(sum - 1))
    hh = (m/sum) * ((m-1)/(sum - 1))
    hr = (n/sum) * ((m)/(sum - 1)) + (m/sum) * ((n)/(sum - 1))

    q = rr + 0.25*hh + 0.5*hr

    return 1 - q


print(probability(15, 19, 29))