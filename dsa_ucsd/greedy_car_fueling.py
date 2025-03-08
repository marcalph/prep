from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    refills, cur_pos = 0, 0
    idx=0
    while cur_pos + tank <distance:
        # Find the farthest reachable station
        next_idx = idx
        while next_idx < len(stops) and stops[next_idx] <= cur_pos + tank:
            next_idx += 1
        
        # If we can't move forward, return -1 (impossible case)
        if next_idx == idx:
            return -1
        
        # Move to the farthest reachable station
        cur_pos = stops[next_idx - 1]
        refills += 1  # Increment refuel count
        idx = next_idx  # Move to next station
    
    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
