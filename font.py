import sys
import time

def escrita(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.09)

texto = 'Murillão é gay pra sempre'
escrita(texto)