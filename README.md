# plaintext-fix
> **Correction de texte par LLM via Ollama en Python**

## Présentation

`plaintext-fix` est un projet qui utilise des modèles de langage (LLM) pour effectuer des corrections de texte. Il est conçu pour fournir une solution simple et efficace pour améliorer la qualité des textes en automatisant les corrections via des outils basés sur l'intelligence artificielle. Ce projet utilise **Ollama**, une plateforme pour intégrer des LLM dans des applications Python.

## Fonctionnalités clés

- Correction automatique de texte en utilisant des modèles de langage.
- Intégration facile avec des scripts en Python.
- Extensible pour différents cas d'utilisation liés à la manipulation de texte.

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/0x07cb/plaintext-fix.git
   cd plaintext-fix
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé) :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer la correction de texte :**
   Le script principal pour exécuter le correcteur de texte peut être trouvé dans le dépôt. Utilisez la commande suivante pour lancer le processus :
   ```bash
   python main.py --input "Votre texte ici"
   ```

2. **Options de ligne de commande :**
   - `--input` : Spécifie le texte à corriger.
   - `--output` : Fichier de sortie pour enregistrer le texte corrigé (optionnel).

3. **Exemple :**
   ```bash
   python main.py --input "Ceci est un exemple de text avec des erreurs." --output corrected_text.txt
   ```

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction de bug :
   ```bash
   git checkout -b ma-nouvelle-fonctionnalite
   ```
3. Faites vos modifications et effectuez un commit :
   ```bash
   git commit -m "Ajout de ma nouvelle fonctionnalité"
   ```
4. Poussez votre branche :
   ```bash
   git push origin ma-nouvelle-fonctionnalite
   ```
5. Ouvrez une Pull Request sur GitHub.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## Remarques supplémentaires

Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue. Bonne correction de texte !

