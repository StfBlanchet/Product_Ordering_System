# Identify catchment area
pos1 = ['75001', '75002', '75003', '75004', '75006', '75007']
pos2 = ['75013', '75014', '75015']
pos3 = ['75011', '75012', '75020']
pos4 = ['75009', '75010', '75018', '75019']
pos5 = ['75008', '75016', '75017']

# Set serving values
small_serving = 1
medium_serving = 1.5
large_serving = 2

# Set pricing values
small_pricing = 0
medium_pricing = 3
large_pricing = 6

# Store input text
set_reception = """

    Faites votre choix :

    1 - commande à emporter
    2 - commande à livrer

    """

set_payment = """

    Je choisis mon mode de paiement :
    
    1 - en ligne
    2 - à réception de ma commande
    
    """

choose_product = """
    
    Choisissez un produit :
    
    1 - Margherita
    2 - Reine
    3 - Napolitaine
    4 - Quatre Saisons
    5 - Végétarienne
    
    """

choose_size = """

    Entrez la taille souhaitée :
    
    1 - small
    2 - medium
    3 - large            
    
    """

add_product = ("""
    
    Souhaitez-vous ajouter un produit ?
    
    1 - Oui
    2 - Non merci, je valide mon panier !
    
    """)


# Messages

welcome_user = """

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    -------------------------
    Bienvenue chez OC Pizza !
    -------------------------
    """

welcome_manager = """

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
    
    ------------------------------
    Bienvenue dans votre Manager !
    ------------------------------
    """

no_stock = """

    Nous sommes désolés. Notre stock est insuffisant pour le produit et la quantité choisis.
    Veuillez modifier votre choix.
    
    """

thanks = """

    OC Pizza vous remercie 
    et vous souhaite bonne dégustation !
                     
    """


validate_order = """

              *************************
              Je valide ma commande (1)
              *************************
            
              """

edit = """
____________________________________________________

                   VOTRE COMMANDE
____________________________________________________

"""

# Lists

ingredient_list = [
    'pâte', 'sauce tomates', 'mozzarella', 'olives', 'jambon', 'champignons', 'artichauts',
    'aubergines', 'courgettes', 'câpres', 'anchois']

order_labels = ['nom', 'taille', 'prix', 'quantité']

order_follow = ['Date', 'Mode de réception', 'Statut commande', 'Montant', 'Mode de paiment', 'Statut paiement']