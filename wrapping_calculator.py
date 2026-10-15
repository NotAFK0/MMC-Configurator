import math

PITCH_DEG = 15.0
WIDTH_OFFSET = 1497.0
HEIGHT_OFFSET = 580.0
POST_SIZE = 50.0
BAY_OFFSET = 295.0


def calculate_wrapping_cuts(width: float, height: float, length: float, bays: int) -> dict:
    """Return cut lengths, member quantities and frame dimensions (mm) for the Wrapping System."""
    if bays <= 0:
        raise ValueError("bays must be a positive integer")

    pitch_rad = math.radians(PITCH_DEG)

    portals = bays + 1
    upright_cut_length = height - HEIGHT_OFFSET
    effective_half_span = (width - WIDTH_OFFSET) / 2
    rafter_cut_length = effective_half_span / math.cos(pitch_rad)
    bay_size = (length - (POST_SIZE * (bays + 1))) / bays
    base_rail_cut_length = bay_size - BAY_OFFSET
    peak_height = height + (width / 2) * math.tan(pitch_rad)

    return {
        "dimensions": {
            "peakHeight": peak_height,
            "baySize": bay_size,
        },
        "portals": portals,
        "cuts": {
            "upright": {"cutLength": upright_cut_length, "qty": 2 * portals},
            "rafter": {"cutLength": rafter_cut_length, "qty": 2 * portals},
            "baseRail": {"cutLength": base_rail_cut_length, "qty": 2 * bays},
        },
    }


if __name__ == "__main__":
    inputs = {"width": 5970, "height": 3000, "length": 6000, "bays": 3}
    result = calculate_wrapping_cuts(**inputs)
    print("Test log")
    print(f"inputs: {inputs}")
    print(f"peakHeight: {result['dimensions']['peakHeight']:.3f} mm")
    print(f"baySize: {result['dimensions']['baySize']:.3f} mm")
    print(f"portals: {result['portals']}")
    for name, cut in result["cuts"].items():
        print(f"{name}: cutLength={cut['cutLength']:.3f} mm, qty={cut['qty']}")
