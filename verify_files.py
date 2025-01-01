import os

# Dossier de base
base_path = 'C:/Users/Utilisateur/Desktop/projet8'

# Vérifier les répertoires train, val, test
for subdir in ['train', 'val', 'test']:
    print(f"\n=== Vérification des images dans le dossier '{subdir}' ===")
    dir_path = os.path.join(base_path, subdir)
    
    for category in os.listdir(dir_path):
        category_path = os.path.join(dir_path, category)
        if os.path.isdir(category_path):
            num_images = len(os.listdir(category_path))
            print(f"Catégorie '{category}': {num_images} images")
