def recommend_style(body_type: str, undertone: str):
    """
    Generates style and color recommendations based on body type and skin undertone.
    """

    recommendations = {
        "fit_guidance": [],
        "color_palette": [],
        "style_aesthetics": []
    }

    # ----- Fit guidance based on body type -----
    if body_type == "Athletic":
        recommendations["fit_guidance"] = [
            "Structured fits",
            "Defined waistlines",
            "Layered outfits"
        ]
        recommendations["style_aesthetics"].append("Sporty Chic")

    elif body_type == "Slim":
        recommendations["fit_guidance"] = [
            "Relaxed fits",
            "Layered silhouettes",
            "Textured fabrics"
        ]
        recommendations["style_aesthetics"].append("Minimal")

    elif body_type == "Curvy":
        recommendations["fit_guidance"] = [
            "Flowy fabrics",
            "Waist-accentuating fits",
            "Soft drapes"
        ]
        recommendations["style_aesthetics"].append("Feminine")

    else:  # Broad
        recommendations["fit_guidance"] = [
            "Vertical lines",
            "Tailored fits",
            "Monochrome outfits"
        ]
        recommendations["style_aesthetics"].append("Classic")

    # ----- Color palette based on undertone -----
    if undertone == "Warm":
        recommendations["color_palette"] = [
            "Olive", "Mustard", "Beige", "Coral", "Brown"
        ]

    elif undertone == "Cool":
        recommendations["color_palette"] = [
            "Navy", "Emerald", "Lavender", "Grey", "Burgundy"
        ]

    else:  # Neutral
        recommendations["color_palette"] = [
            "Black", "White", "Taupe", "Denim Blue"
        ]

    return recommendations
