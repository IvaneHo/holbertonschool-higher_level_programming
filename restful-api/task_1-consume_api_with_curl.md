1. Consume data from an API using command line tools (curl)

---

1. Installation et test de curl

Sur mon système (Linux ou WSL), j’ai installé curl avec la commande :
sudo apt install curl

Ensuite, j’ai vérifié la version installée :
curl --version

Sortie obtenue (exemple) :
curl 7.81.0 (x86_64-pc-linux-gnu) libcurl/7.81.0 OpenSSL/1.1.1n zlib/1.2.11
Protocols: http https
Features: IPv6 SSL libz

---

2. Récupérer le contenu d’une page web

Commande utilisée :
curl http://example.com

Résultat : le HTML brut de la page `example.com` est affiché dans le terminal.

---

3. Récupérer des données depuis une API

Commande :
curl https://jsonplaceholder.typicode.com/posts

Résultat :
Un tableau JSON contenant des publications. Chaque élément contient :
- userId
- id
- title
- body

Extrait :
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati...",
    "body": "quia et suscipit..."
  },
  ...
]

---

4. Récupérer uniquement les en-têtes HTTP (headers)

Commande :
curl -I https://jsonplaceholder.typicode.com/posts

Exemple de sortie :
HTTP/2 200 
date: Mon, 09 Jun 2025 07:35:12 GMT
content-type: application/json; charset=utf-8
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999

Cela montre les informations sans le contenu, ce qui est utile pour diagnostiquer les serveurs.

---

5. Envoyer une requête POST avec des données

Commande :
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Résultat :
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}

Remarque : JSONPlaceholder est un faux service API, donc il renvoie une réponse simulée mais ne crée rien en réalité.

---

Conclusion :

Cet exercice m’a permis de :
- Installer et tester curl
- Faire des requêtes GET simples
- Lire les en-têtes HTTP
- Envoyer des données via POST
- Mieux comprendre comment interagir avec des API REST depuis la ligne de commande

Fin du fichier.
