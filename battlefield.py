import json
import random
import time

class Ship:
    def __init__(self, name, power, armor):
        self.name = name
        self.power = power
        self.armor = armor
        self.is_drowning = False
        self.drowning_steps = 0

    def hit(self, damage):
        self.armor -= damage
        if self.armor <= 0:
            self.is_drowning = True

    def shoot(self):
        return random.uniform(0.25, 1.0) * self.power

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Armor: {self.armor}, Drowning: {self.is_drowning})"

class Team:
    def __init__(self, name, ships):
        self.name = name
        self.ships = ships

    def remove_drowning_ships(self):
        self.ships = [ship for ship in self.ships if not (ship.is_drowning and ship.drowning_steps >= 2)]

    def __str__(self):
        return f"{self.name} with ships: {[str(ship) for ship in self.ships]}"

def load_teams_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        teams = []
        for team_data in data['teams']:
            ships = [Ship(ship['name'], ship['power'], ship['armor']) for ship in team_data['ships']]
            teams.append(Team(team_data['name'], ships))
        return teams

def simulate_battle(teams):
    iteration = 0
    while all(len(team.ships) > 0 for team in teams):
        iteration += 1
        print(f"\nIteration {iteration}")

        for team in teams:
            for ship in team.ships:
                if ship.is_drowning:
                    ship.drowning_steps += 1
                if len([enemy_ship for enemy_team in teams if enemy_team != team for enemy_ship in enemy_team.ships]) > 0:
                    enemy_team = random.choice([enemy_team for enemy_team in teams if enemy_team != team])
                    enemy_ship = random.choice(enemy_team.ships)
                    damage = ship.shoot()
                    enemy_ship.hit(damage)
                    print(f"{ship.name} from {team.name} hit {enemy_ship.name} from {enemy_team.name} with {damage:.2f} damage.")
        
        for team in teams:
            team.remove_drowning_ships()

    for team in teams:
        if len(team.ships) == 0:
            print(f"\n{team.name} has been defeated!")
        else:
            print(f"\n{team.name} is victorious!")

# Example usage:
file_path = 'ships_data.json'  # Ensure you have this JSON file with the appropriate structure
teams = load_teams_from_json(file_path)
simulate_battle(teams)
