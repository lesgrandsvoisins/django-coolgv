from django.core.exceptions import ValidationError

def validate_svg(file):
    # Read some bytes and try to decode as text (SVG is XML)
    try:
        content = file.read().decode('utf-8')
    except UnicodeDecodeError:
        raise ValidationError("The uploaded file is not a valid SVG (not UTF-8 text).")

    if not content.strip().startswith("<svg"):
        raise ValidationError("The uploaded file does not appear to be a valid SVG file.")

    # Reset the file pointer for further use (important!)
    file.seek(0)