import numpy as np


def overlapping_duration(starts, stops):
    return total_duration(*np.array(overlapping_periods(starts, stops)).T)

def overlapping_periods(starts, stops): #-> Iterable[Tuple[Datetime, Datetime]]:
    periods = []
    start, stop = starts[0], stops[0]
    for a, b in zip(starts, stops):
        if a > stop:
            periods.append((start, stop))
            # print(f"{start}\t{stop}\t{stop - start}")
            start, stop = a, b
        else:
            stop = b
    else:
        periods.append((start, stop))
        # print(f"{start}\t{stop}\t{stop - start}")
    return periods


def total_duration(starts, stops, unit='s') -> int:
    deltas = np.array(stops) - np.array(starts)
    return deltas.sum().astype(f'timedelta64[{unit}]')
