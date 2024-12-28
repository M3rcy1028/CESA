import time

def chebyshev_128_bit():

    # Initialize 128-bit values
    x = 0x123456789ABCDEF123456789ABCDEF1  # x value for Chebyshev recursion
    Tn_minus_2 = 1  # T0(x)
    Tn_minus_1 = x  # T1(x)
    prime_modulus = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC5  # Large 128-bit prime modulus

    print(f"Initial T0(x): {Tn_minus_2}")
    print(f"Initial T1(x): {Tn_minus_1}")
    print(f"Prime Modulus: {hex(prime_modulus)}")

    # Perform Chebyshev recursion
    for i in range(10000):
        Tn = 2 * x * Tn_minus_1 - Tn_minus_2
        Tn_minus_2 = Tn_minus_1
        Tn_minus_1 = Tn % prime_modulus  # Apply modulus to avoid overflow


def chebyshev_256_bit():
    # Initialize 512-bit values
    x = 0x123456789ABCDEF123456789ABCDEF123456789ABCDEF123456789ABCDEF1234  # x value for Chebyshev recursion
    Tn_minus_2 = 1  # T0(x)
    Tn_minus_1 = x  # T1(x)
    prime_modulus = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF  # Large 512-bit prime modulus

    print(f"Initial T0(x): {Tn_minus_2}")
    print(f"Initial T1(x): {Tn_minus_1}")
    print(f"Prime Modulus: {hex(prime_modulus)}")

    # Perform Chebyshev recursion
    
    for i in range(10000):
        Tn = 2 * x * Tn_minus_1 - Tn_minus_2
        Tn_minus_2 = Tn_minus_1
        Tn_minus_1 = Tn % prime_modulus  # Apply modulus to avoid overflow
    

    


if __name__ == "__main__":
    
    start_time = time.time()
    print("---------------------------------------------------------")
    print("Chebyshev 128-bit Computation")
    chebyshev_128_bit()
    elapsed_time = (time.time() - start_time) * 1000  # Convert seconds to microseconds
    print(f"Execution Time: {elapsed_time:.2f} µs")

    start_time = time.time()
    print("---------------------------------------------------------")
    print("Chebyshev 256-bit Computation")
    chebyshev_256_bit()
    elapsed_time = (time.time() - start_time) * 1000  # Convert seconds to microseconds
    print(f"Execution Time: {elapsed_time:.2f} µs")
