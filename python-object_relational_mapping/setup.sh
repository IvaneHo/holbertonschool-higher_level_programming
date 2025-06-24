#!/bin/bash

echo "🔧 Création d'un environnement virtuel .venv..."
python3 -m venv .venv

echo "✅ Environnement virtuel créé."

echo "📦 Activation de l'environnement virtuel..."
source .venv/bin/activate

echo "📥 Installation des dépendances (mysqlclient, SQLAlchemy)..."
pip install --upgrade pip
pip install mysqlclient SQLAlchemy

echo "✅ Paquets installés."

echo "🔍 Vérification de l'import de MySQLdb..."
python3 -c "import MySQLdb; print('✔️ MySQLdb importé avec succès ! Version :', MySQLdb.version_info)"

echo "📝 Enregistrement des dépendances dans requirements.txt..."
pip freeze > requirements.txt

echo "🎉 Environnement prêt !"
echo "👉 Pour activer le venv plus tard : source .venv/bin/activate"
