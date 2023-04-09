import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='kLGxoNfP28Vu7H0LYRouNQ',
                     client_secret='XeOtT0OLRbIprxlEDdRRmh4XzFr5pQ',
                     user_agent='TestingAlaxos')

subreddit = reddit.subreddit('monterrey')

posts_with_software = subreddit.search('rayados', limit=10000)

count = 0

for post in posts_with_software:
    count += 1

posts_with_software2 = subreddit.search('tigres', limit=10000)

conteo = 0

for post in posts_with_software2:
    conteo += 1

posts_with_software3 = subreddit.search('america', limit=10000)

contador = 0

for post in posts_with_software3:
    contador += 1

print(f'El número total de posts con la palabra "rayados": {count}')
print(f'El número total de posts con la palabra "tigres": {conteo}')
print(f'El número total de posts con la palabra "america": {contador}')

# Datos a graficar
labels = ['rayados', 'tigres', 'america']
values = [count, conteo, contador]

# Crear la gráfica de barras
fig, ax = plt.subplots()
ax.bar(labels, values)

# Agregar etiquetas de datos
for i, v in enumerate(values):
    ax.text(i, v, str(v), ha='center', va='bottom')

# Agregar título y etiquetas a los ejes
ax.set_title('Conteo de palabras en r/monterrey')
ax.set_xlabel('Palabras')
ax.set_ylabel('Conteo')

# Mostrar la gráfica
plt.show()