# Name: Revanth
# Email ID: revanth.rs.2026

def get_suitable_rooms(rooms, num_students):
    """
    Creates a list of suitable study rooms

    Args:
        rooms (list[tuple]): A list of tuples representing study rooms. Each tuple
        contains 4 elements: (room_name, capacity, has_projector, is_available)
    
    Returns:
        list[str]: a list of study room names satisfying the criteria

    """
    suitable_rooms = []
    for room in rooms:
        name, capacity, has_projector, is_available = room
        if capacity >= num_students and has_projector and is_available:
            suitable_rooms.append(name)
            
    return suitable_rooms
        
