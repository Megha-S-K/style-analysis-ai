def generate_style_explanation(body_type_result, skin_result, style_recommendation):
    """
    Generates a human-friendly explanation using structured inputs.
    This function is LLM-ready but safe and deterministic for now.
    """

    body_type = body_type_result["body_type"]
    body_conf = body_type_result["confidence"]

    undertone = skin_result["undertone"]
    skin_conf = skin_result["confidence"]

    fits = ", ".join(style_recommendation["fit_guidance"])
    colors = ", ".join(style_recommendation["color_palette"])
    aesthetics = ", ".join(style_recommendation["style_aesthetics"])

    explanation = (
        f"Based on the image analysis, your body structure aligns most closely "
        f"with a **{body_type}** profile (confidence: {int(body_conf * 100)}%). "
        f"This suggests that styles such as {fits.lower()} tend to complement "
        f"your natural proportions.\n\n"
        f"Your skin undertone appears to be **{undertone.lower()}** "
        f"(confidence: {int(skin_conf * 100)}%), which means colors like "
        f"{colors.lower()} are likely to suit you well.\n\n"
        f"Overall, styles within the **{aesthetics}** aesthetic should feel "
        f"balanced and natural on you. These suggestions are meant as guidance, "
        f"and personal comfort and preference should always come first."
    )

    return explanation
