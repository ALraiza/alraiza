import random

def sampah_organik():
    nama_sampah = ['daun', 'sayur busuk', 
                    'buah busuk', 'nasi basi',
                    'bangkai', 'kotoran hewan',
                    'ranting pohon', 'limbah ternak', 
                    'tulang', 'kulit buah', 'cangkang telur',
                    'ampas kopi', 'ampas teh']
    return random.choice(nama_sampah)

def sampah_anorganik():
    nama_sampah = ['plastik' 'styrofoam', 'kaleng',
                   'kertas', 'kaca', 'keramik', 'besi',
                   'botol plastik', 'kardus',]
     return random.choice(nama_sampah)
