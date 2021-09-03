VALID_POSITIONS = ['a', 'b', 'c']


# Function to sort a list of dicts
def sort_list_of_dicts(dict_to_sort, key_to_use):
    return sorted(dict_to_sort, key=lambda x: x[key_to_use])


# Function that determines the fate of our autonomous car
# Takes the track and travel log as arguments
def car_route_result(track, travel_log):
    # Our car's starting position
    car_pos = ('b', 0)
    try:
        # If track and travel log are both empty, return error
        if len(track) == 0 and len(travel_log) == 0:
            return {"status": "error", "message": "Race track and obstacles missing"}

        # This is done as a precaution. What if track and travel log are not sorted
        # according to position. If we are sure they will always be sorted, we can remove them.
        track = sort_list_of_dicts(track, 'position')
        travel_log = sort_list_of_dicts(travel_log, 'position')

        # Calculate the max position to which our car is going to travel to. A simple max function
        # that returns the maximum of the position in the last 2 dicts
        max_position = max(track[-1]['position'] if len(track) != 0 else 0,
                           travel_log[-1]['position'] if len(travel_log) != 0 else 0) + 1
        failure_position = 0

        # Iterate over each position on the track
        for position in range(max_position):
            # Check if travel log array is not empty and if it has data for the current position
            # of our car
            if len(travel_log) != 0 and position == travel_log[0]['position']:
                # Change lanes by +/- the ASCII of the lane
                if travel_log[0]['laneChange'] == 'left':
                    car_pos = (chr(ord(car_pos[0]) - 1), position)
                elif travel_log[0]['laneChange'] == 'right':
                    car_pos = (chr(ord(car_pos[0]) + 1), position)
                # Check if the car goes out of bounds
                if car_pos[0] not in VALID_POSITIONS:
                    failure_position = position
                    return {"status": "error", "position": str(failure_position)}
                del travel_log[0]
            else:
                car_pos = (car_pos[0], position)

            # Check if travel log array is not empty and if it has data for the current position
            if len(track) != 0 and position == track[0]['position']:
                # Check if f car encounters obstacle
                if car_pos[0] in track[0]['obstacles']:
                    failure_position = position
                    return {"status": "error", "position": str(failure_position)}
                del track[0]
        return {"status": "success"}
    except Exception as e:
        print(e)
