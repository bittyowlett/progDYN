def map_generate(f,seed,N):
    x0 = seed 
    x = [x0]
    i=1
        while i<N:
        rel = f(x0)
        x.append(rel)
        x0 = rel
        i += 1
    return x