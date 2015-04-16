from random import randint

world   = {}
width   = 90
height  = 45
plt_nrg = 80
rep_nrg = 200

def draw_world(world):
    for y in range(height):
        print("|", end="")
        for x in range(width):
            if world[(x,y)][0]:
                print("M", end="")
            elif world[(x,y)][1]:
                print("*", end="")
            else:
                print(" ", end="")
        print("|\n", end="")

def simulate_day():
    add_plants()
    
    for key, value in world.items():
        if value[0]:
            turn_animal(key)
            eat_animal(key)
            reproduce_animal(key)
            check_for_dead(key)
            move_animal(key)
            
def organism_count():
    a_count = 0
    p_count = 0
    for key, value in world.items():
        if value[0]:
            a_count += 1
        if value[1]:
            p_count += 1
    print("Animals: {}, Plants: {}".format(a_count, p_count))
        
def move_animal(key):
    
    # Add logic for deciding which way to move
    x,y = (key[0] + 1) % width, (key[1] + 1) % height
    
    moved = world[key].copy()
    
    moved[1] = world[x,y][1]
    moved[2] -= 1
    world[(x,y)] = moved
    
    world[key][0] =  False

def turn_animal(key):
    
    # Add logic to decide how to turn
    world[key][3] = (world[key][3] + 1) % 8

def eat_animal(key):
    
    if world[key][0] and world[key][1]:
        world[key][2] += plt_nrg
        world[key][1] = False
        
def reproduce_animal(key):
    
    if world[key][2] > rep_nrg:
        world[key][2] = int(world[key][2] / 2)
        copy_animal(key)
        
def copy_animal(key):
    
    #just like the move function
    x,y = (key[0] - randint(1,4)) % width, (key[1] - randint(1,4)) % height
    
    moved = world[key].copy()
    
    moved[1] = world[x,y][1]
    moved[2] -= 1
    world[(x,y)] = moved

def check_for_dead(key):
    if world[key][2] < 1:
        world[key][0] = False
        
def add_plants():
    
    x, y = randint(1, width - 1), randint(1, height - 1)
    j_x, j_y = randint(int(width / 3), int(width / 2)), randint(int(height / 3), int(height / 2))
    
    world[(x,y)][1] = True
    world[(j_x,j_y)][1] = True

def main(argv=None):
    
    # Randomly generate a set of genes for the first animal
    genes = [randint(1,8) for i in range(8)]
    
    # Initialize the whole world
    for x in range(width):
        for y in range(height):
            world[(x,y)] = [False, False, 1000, 0, genes]
    
    # Add the first animal - right in the middle
    world[(int(width / 2), int(height / 2))][0] = True
    
    day_count = 0
    # loop forever
    while True:
        num = input('Days:')
        day_count += int(num)
        for i in range(int(num)):
            simulate_day()
            
        print("Days: {} Years: {}".format(day_count, int(day_count / 365)))
        organism_count()
        draw_world(world)
    
if __name__ == "__main__":
    main()