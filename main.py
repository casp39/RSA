from math import gcd

def lcm(p, q):

    return p * q // gcd (p, q)

def generate_keys(p, q):
    N = p * q
    L = lcm(p-1, q-1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    return (E, N), (D, N)

def encrypt(plain_number, public_key):
  E, N = public_key
  encrypted_number = pow(plain_number, E, N)

  return encrypted_number

def decrypt(encrypted_number, private_key):
  D, N = private_key
  decrypted_number = pow(encrypted_number, D, N)

  return decrypted_number

if __name__ == '__main__':
  plain_number = int(input('Please Enter Plain Number: '))

  print('Please Enter Two Prime Numbers: ')
  p, q = (int(i) for i in input().split())
  public_key, private_key = generate_keys(p, q)

  encrypted_number = encrypt(plain_number, public_key)
  decrypted_number = decrypt(encrypted_number, private_key)

  print('Encrypted Number: {}, Decrypted Number: {}'.format(encrypted_number, decrypted_number))
