0. Basics of HTTP/HTTPS

---

1. Différences entre HTTP et HTTPS

HTTP (HyperText Transfer Protocol) est un protocole utilisé pour transférer des données sur le web. Il n'offre aucune sécurité : les données circulent en texte clair, ce qui les rend vulnérables à l'interception.

HTTPS (HyperText Transfer Protocol Secure) est une version sécurisée de HTTP. Il utilise TLS/SSL pour chiffrer les échanges entre le client (navigateur) et le serveur, empêchant les attaques de type "man-in-the-middle", le vol de données ou les modifications non autorisées.

Principales différences :
- HTTP utilise le port 80, HTTPS le port 443
- HTTP ne chiffre pas les données ; HTTPS chiffre tout le contenu échangé
- HTTPS utilise un certificat SSL/TLS pour authentifier l'identité du site
- Les URLs commencent par http:// (non sécurisé) ou https:// (sécurisé)

---

2. Structure d’une requête et réponse HTTP

Requête HTTP :
GET /hello.txt HTTP/1.1
Host: www.example.com
User-Agent: curl/7.63.0
Accept-Language: en

Réponse HTTP :
HTTP/1.1 200 OK
Date: Wed, 30 Jan 2019 12:14:39 GMT
Server: Apache
Content-Type: text/plain
Content-Length: 12

Hello World!

Note : en HTTP, tout ceci est lisible par n’importe qui. En HTTPS, le contenu est entièrement chiffré.

---

3. Méthodes HTTP courantes

- GET : récupère une ressource. Exemple : afficher une page web.
- POST : envoie des données au serveur. Exemple : formulaire de connexion.
- PUT : modifie ou remplace une ressource. Exemple : mise à jour d’un profil.
- DELETE : supprime une ressource. Exemple : suppression d’un message.

---

4. Codes d’état HTTP courants

- 200 OK : La requête a réussi. Exemple : chargement d’une page.
- 301 Moved Permanently : La ressource a été déplacée définitivement.
- 400 Bad Request : La requête est mal formulée. Exemple : erreur dans un formulaire.
- 404 Not Found : La ressource demandée est introuvable.
- 500 Internal Server Error : Une erreur s’est produite côté serveur.

---

Fin du fichier.
