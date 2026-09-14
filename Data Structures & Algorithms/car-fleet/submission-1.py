class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = sorted(zip(position, speed), reverse=True)
        arrival = []
        for pos, spd in positions:
            arrival_time = (target - pos)/spd
            if not arrival or arrival_time > arrival[-1]:
                arrival.append(arrival_time)
        return len(arrival)
