from prime_gen import n_bit_prime
import random
import math
import sympy

##RSA KEYGEN
P_Q_SIZE = 1024

# Verifica se 2 números são coprimos
def is_coprime(x, y):
    if math.gcd(x, y) == 1:
        return True
    return False

# Calcula E com o totient function de P e Q
def E(T):
    while True:
        num = random.randrange(1, T - 1)
        if is_coprime(num, T):
            break
    return num

P = n_bit_prime(P_Q_SIZE)
Q = n_bit_prime(P_Q_SIZE)

N = P * Q
T = (P - 1)*(Q - 1)

E = E(T)
D = pow(E, -1, T)

PUBLIC = [E,N]
PRIVATE = [D,N]
KEYS = [PUBLIC, PRIVATE]

def print_vars(P,Q,N,T,E,D):
    print('P:')
    print(P) 
    print('Q:')
    print(Q) 
    print('N:')
    print(N) 
    print('T:')
    print(T) 
    print('E:')
    print(E) 
    print("PUBLIC KEY:")
    print(PUBLIC)
    print("PRIVATE KEY:")
    print(PRIVATE)

def test_vars(P, Q, N, T, E, D):
    print( "P  Q are primes?")
    print( sympy.isprime(P), sympy.isprime(Q))
    print( "P * Q == N ?")
    print( P * Q == N)
    print( "E e T são coprimos e 1<E<T?")
    print( is_coprime(E,T), 1 < E and E < T)
    print( "E *D == 1 mod T ?")
    print( (E * D) % T == 1)

print_vars(P,Q,N,T,E,D)
#test_vars(P,Q,N,T,E,D)

def get_keys():
    return KEYS

##AES KEYGEN
def n_bit_random(n):
    n = 32
    return random.getrandbits(n)
