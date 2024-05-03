import matplotlib.pyplot as plt


def moveNautilus():

    # Paramètres du sous-marin
    masse = 50000000  
    volume = 50000  

    # Constantes
    g = 9.81  
    rho = 1000 

    # Durée des phases en secondes
    duree_phase = 280 

    # Initialisation des puissances des moteurse en Newton
    puissance_max_x = 10000000  
    puissance_max_y = 300000  
    puissance_min_y = -300000  

    # Initialisation du temps
    temps = 0

    # Initialisation de la position et de la vitesse
    position = [0, 0]  
    vitesse = [0, 0]  

    # Enregistrement des positions
    positions = [position.copy()]
    phase_positions = [] 

    # Simulation du mouvement du sous-marin
    dt = 1
    while temps <= (8 * duree_phase):

        force_moteur_x, force_moteur_y = 0, 0
        
        # Phase 1
        if temps < duree_phase:
            force_moteur_y = puissance_min_y * (temps / duree_phase)
            
        # Phase 2
        elif temps < 2 * duree_phase:
            force_moteur_x = puissance_max_x * ((temps - duree_phase) / duree_phase)
            
        # Phase 3
        elif temps < 6 * duree_phase:
            force_moteur_x = puissance_max_x

            if vitesse[1] >= 0:
                force_moteur_y = puissance_min_y 
            elif vitesse[1] <= 0:
                force_moteur_y = puissance_max_y
            else:
                force_moteur_y = 0
                
        # Phase 4
        elif temps < 7 * duree_phase:
            force_moteur_x = puissance_max_x * (1 - (temps - 4 * duree_phase) / duree_phase) 
            force_moteur_y = puissance_max_y * ((temps - 3 * duree_phase) / duree_phase) 
        
        # Phase 5
        else:
            force_moteur_x = puissance_max_x * (1 - (temps - 4 * duree_phase) / duree_phase) 

        # Calcul de la poussée d'Archimède
        poussee_archimede = volume * rho * g

        # Calcul de la force nette sur le sous-marin
        force_nette_x = force_moteur_x
        force_nette_y = force_moteur_y + poussee_archimede - masse * g

        # Calcul de l'accélération du sous-marin
        acceleration_x = force_nette_x / masse
        acceleration_y = force_nette_y / masse

        # Mise à jour de la vitesse et de la position
        vitesse[0] += acceleration_x * dt
        vitesse[1] += acceleration_y * dt
        position[0] += vitesse[0] * dt
        position[1] += vitesse[1] * dt
        if position[1] > 0 : 
            position[1] = 0
        positions.append(position.copy())

        # Si c'est un changement de phase, enregistrer la position actuelle
        if temps % duree_phase == 0:
            phase_positions.append(position.copy())

        # Mise à jour du temps
        temps += dt

    # Tracé de la trajectoire du sous-marin
    plt.figure(figsize=(10, 6))
    plt.plot([pos[0] for pos in positions], [pos[1] for pos in positions])
    plt.scatter([pos[0] for pos in phase_positions], [pos[1] for pos in phase_positions], color='red', label='Changements de phase')
    plt.xlabel('Position en X (m)')
    plt.ylabel('Profondeur (m)')
    plt.title('Trajectoire du Nautilus')
    plt.legend()
    plt.grid(True)
    plt.show()


moveNautilus()