class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort in descending order based on starting position
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0.0  # Keeps track of the time taken by the slowest lead car/fleet
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If this car takes strictly longer than the fleet ahead,
            # it will never catch up. It forms a new fleet.
            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target
                
        return fleets
