import random

def sampah_organik():
    nama_sampah = ['daun', 'sayur busuk', 
                    'buah busuk', 'nasi basi',
                    'bangkai', 'kotoran hewan',
                    'ranting pohon', 'limbah ternak', 
                    'tulang', 'kulit buah', 'cangkang telur',
                    'ampas kopi', 'ampas teh']
    return random.choice(nama_sampah)
