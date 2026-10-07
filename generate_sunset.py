from PIL import Image, ImageDraw

def create_gradient(width, height, start_color, end_color):
    """Creates a vertical gradient."""
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), start_color)
    bottom = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(bottom, (0, 0), mask)
    return base

def generate_sunset(filename="sunset.png", width=800, height=600):
    # Colors
    sky_top = (25, 25, 112)      # Midnight Blue
    sky_mid = (147, 112, 219)    # Medium Purple
    sky_horizon = (255, 69, 0)   # Red-Orange
    sun_color = (255, 215, 0)    # Gold
    ground_color = (0, 0, 0)     # Black

    # Create sky gradient (Top to Mid)
    img = create_gradient(width, height, sky_top, sky_horizon)
    
    draw = ImageDraw.Draw(img)

    # Draw Sun
    sun_radius = 50
    sun_x = width // 2
    sun_y = int(height * 0.7)
    draw.ellipse(
        (sun_x - sun_radius, sun_y - sun_radius, sun_x + sun_radius, sun_y + sun_radius),
        fill=sun_color,
        outline=None
    )

    # Draw Mountains/Ground (Simple polygon)
    mountains = [
        (0, height),
        (0, int(height * 0.75)),
        (int(width * 0.2), int(height * 0.6)),
        (int(width * 0.4), int(height * 0.8)),
        (int(width * 0.6), int(height * 0.65)),
        (int(width * 0.8), int(height * 0.85)),
        (width, int(height * 0.7)),
        (width, height)
    ]
    draw.polygon(mountains, fill=ground_color)

    # Save
    img.save(filename)
    print(f"Sunset image saved to {filename}")

if __name__ == "__main__":
    generate_sunset()
