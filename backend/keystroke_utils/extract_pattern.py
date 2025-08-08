def extract_keystroke_pattern(key_events):
    # Converts key events into time delta list
    # Example: [100, 120, 115, ...]
    return [int(t) for t in key_events]
