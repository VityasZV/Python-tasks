def turtle(coord, direction):
    command = None
    new_command = yield command
    while new_command:
        new_coordinates = list(coord) #now its old
        if new_command == "f":
            if direction == 0:
                new_coordinates[0] += 1
            elif direction == 1:
                new_coordinates[1] += 1
            elif direction == 2:
                new_coordinates[0] -= 1
            elif direction == 3:
                new_coordinates[1] -= 1
        elif new_command == "l":
            direction = (direction + 1) % 4
        elif new_command == "r":
            direction = (direction - 1) % 4
        command = tuple(new_coordinates)
        coord = command
        new_command = yield command
