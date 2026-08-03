def generate_primes(n_primes):
    """Generates the first N prime numbers sequentially."""
    primes = []
    candidate = 2
    while len(primes) < n_primes:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


def hilbert_3d_decode(index, bits=13):
    """
    Decodes a 1D Hilbert distance index into 3D (X, Y, Z) coordinates.
    Based on John Skilling's space-filling curve bitwise transformation.
    """
    X = [0, 0, 0]
    # Step 1: Deinterleave the bits of the index across the 3 dimensions
    for i in range(bits):
        for j in range(3):
            if (index & (1 << (i * 3 + j))) != 0:
                X[j] |= (1 << i)
                
    # Step 2: Inverse Gray decode the structure
    q = 1 << (bits - 1)
    while q > 1:
        p = q - 1
        for i in range(3):
            if (X[i] & q) != 0:
                X[0] ^= p  # Invert low bits
            else:
                t = (X[0] ^ X[i]) & p
                X[0] ^= t
                X[i] ^= t
        q >>= 1
    return X[0], X[1], X[2]


def map_primes_to_cuboid(primes, x_max=4096, y_max=256, z_max=4096):
    """
    Traverses the Hilbert curve path, placing sequential prime numbers
    only at the valid grid nodes inside the uneven cuboid.
    """
    mapped_points = []
    prime_index = 0
    hilbert_index = 0
    total_primes = len(primes)

    # Loop until all input primes are successfully placed inside the boundaries
    while prime_index < total_primes:
        # Get coordinates for the current step along the 3D Hilbert path
        x, y, z = hilbert_3d_decode(hilbert_index, bits=13)
        
        # Boundary constraints check (Inclusive check for 0 to MAX limits)
        if x <= x_max and y <= y_max and z <= z_max:
            current_prime = primes[prime_index]
            mapped_points.append({
                "prime": current_prime,
                "coord": (x, y, z)
            })
            prime_index += 1
            
        # Move to the next step along the space-filling path
        hilbert_index += 1
        
    return mapped_points


# --- EXECUTION EXAMPLE ---
if __name__ == "__main__":
    # Generate a small pool of primes to demonstrate the distribution script
    test_primes = generate_primes(10)
    
    print(f"Mapping the first {len(test_primes)} primes into the cuboid path...")
    results = map_primes_to_cuboid(test_primes, x_max=4096, y_max=256, z_max=4096)
    
    print(f"\n{'Prime Number':<15} | {'(X, Y, Z) Coordinate':<20}")
    print("-" * 40)
    for res in results:
        print(f"{res['prime']:<15} | {str(res['coord']):<20}")
