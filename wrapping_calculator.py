import math

PITCH_DEG = 15.0
WIDTH_OFFSET = 1497.0
HEIGHT_OFFSET = 580.0
POST_SIZE = 50.0
BAY_OFFSET = 295.0


def calculate_wrapping(width: float, height: float, length: float, bays: int) -> dict:
    """Return cut lengths (mm) for the Wrapping System.

    Keys: uprightCutLength, rafterCutLength, baseRailCutLength.
    """
    if bays <= 0:
        raise ValueError("bays must be a positive integer")

    upright_cut_length = height - HEIGHT_OFFSET
    effective_half_span = (width - WIDTH_OFFSET) / 2
    rafter_cut_length = effective_half_span / math.cos(math.radians(PITCH_DEG))
    bay_size = (length - (POST_SIZE * (bays + 1))) / bays
    base_rail_cut_length = bay_size - BAY_OFFSET

    return {
        "uprightCutLength": upright_cut_length,
        "rafterCutLength": rafter_cut_length,
        "baseRailCutLength": base_rail_cut_length,
    }


if __name__ == "__main__":
    inputs = {"width": 5970, "height": 3000, "length": 6000, "bays": 3}
    result = calculate_wrapping(**inputs)
    print("Test log")
    print(f"inputs: {inputs}")
    for key, value in result.items():
        print(f"{key}: {value:.3f} mm")
