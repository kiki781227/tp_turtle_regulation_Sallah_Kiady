# tp_turtle_regulation_Sallah_Kiady


## Partie 1 - Question 7

- Pour un Kp élevé, => la tortue s'oriente rapidement , dépasse le waypoint, puis revient dessus. En résumé, elle tourne sur elle-même.

- Pour un Kp faible => La tortue met du temps à s’orienter vers le waypoint, mais elle finit par se placer correctement dessus

- Le Kp choisi est de 2. La tortue s'oriente a une vitesse considerable et se pointe correctement vers le waypoint

## Partie 2 - Question 5

- Pour un Kpl élevé, => La tortue se dirige en bas a gauche

- Pour un Kpl faible => La tortue se dirige en haut a droite

- Le Kpl choisi est de -1 La tortue se dirge donc en haut a droite

## Etapes pour utiliser les packages

### Installation
Creer un ros workspace:
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```

Aller dans le dossier src et clone le repo:
```bash
cd ~/ros2_ws/src
git clone https://github.com/kiki781227/tp_turtle_regulation_Sallah_Kiady.git
```

Revenir a la racine du workspace:
```bash
cd ~/ros2_ws/
colcon build
```

### Pour tester le subscriber/publisher
Ouvrir l'interface de turtlesim sur un terminal:
```bash
ros2 run turtlesim turtlesim_node
```

Ouvrir un autre terminal: 
```bash
ros2 run turtle_regulation tt1_pub_node 
```

