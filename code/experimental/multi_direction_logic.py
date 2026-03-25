from collections import defaultdict, deque

def choose_lanes_dynamic(lanes, speeds, arrival_times):
    # Create a dictionary to store lanes with vehicle info (arrival time and speed)
    lane_queues = defaultdict(deque)
    
    for lane, speed, arrival in zip(lanes, speeds, arrival_times):
        lane_queues[lane].append((arrival, speed))
    
    # Sort each lane's vehicles by arrival time
    for lane in lane_queues:
        lane_queues[lane] = deque(sorted(lane_queues[lane], key=lambda x: x[0]))
    
    # Prepare to process vehicles
    processed_order = []
    
    while any(lane_queues.values()):  # While there are vehicles in any lane
        earliest_vehicle = None
        selected_lane = None
        
        # Find the earliest vehicle across all lanes
        for lane, queue in lane_queues.items():
            if queue:
                if earliest_vehicle is None or queue[0][0] < earliest_vehicle[0]:
                    earliest_vehicle = queue[0]
                    selected_lane = lane
        
        # Process the vehicle with the earliest arrival time
        if selected_lane is not None:
            lane_queues[selected_lane].popleft()  # Remove the processed vehicle
            processed_order.append(selected_lane)  # Log the lane used
    
    # Generate the lane picking order as a string
    lane_order = " -> ".join(map(str, processed_order))
    return lane_order


# Input handling
total_lanes = int(input("Enter the total number of lanes: "))
num_vehicles = int(input("Enter the number of vehicles: "))

lane_numbers = []
vehicle_speeds = []
arrival_times = []

for i in range(num_vehicles):
    lane_number = int(input(f"Enter lane number for vehicle {i+1}: "))
    speed = float(input(f"Enter speed (km/hr) for vehicle {i+1}: "))
    arrival_time = float(input(f"Enter arrival time (seconds) for vehicle {i+1}: "))
    lane_numbers.append(lane_number)
    vehicle_speeds.append(speed)
    arrival_times.append(arrival_time)

lane_choosing_order = choose_lanes_dynamic(lane_numbers, vehicle_speeds, arrival_times)

print(f"\nLane order to capture all incoming vehicles: {lane_choosing_order}")