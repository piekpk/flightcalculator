"""Utilities for calculating active drone flight time based on payload weight."""


def calculate_flight_time(weight_grams):
    """Return the active flight time in minutes for a given payload weight.

    Parameters:
        weight_grams (float | int): Payload weight in grams. This value must be
            non-negative.

    Returns:
        float: The active flight time in minutes. If the formula would produce a
        negative value, the result is clamped to 0.

    Raises:
        ValueError: If weight_grams is negative.
    """
    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative.")

    flight_time = 180 - 0.1 * weight_grams
    return max(0, flight_time)


def flight_time_table(max_weight_grams, step_grams):
    """Return a list of (weight, flight_time) pairs from 0 through max_weight_grams.

    Parameters:
        max_weight_grams (float | int): Maximum payload weight in grams to include.
        step_grams (float | int): Increment between weights in grams.

    Returns:
        list[tuple[float | int, float]]: A list of (weight, flight_time) pairs,
        where each flight time is calculated by calling calculate_flight_time().
    """
    if max_weight_grams < 0:
        raise ValueError("max_weight_grams must be non-negative.")
    if step_grams <= 0:
        raise ValueError("step_grams must be greater than 0.")

    table = []
    current_weight = 0

    while current_weight <= max_weight_grams:
        table.append((current_weight, calculate_flight_time(current_weight)))
        current_weight += step_grams

    return table