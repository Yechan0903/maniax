from django import template

register = template.Library()

@register.filter
def display_time(total_minutes):
    try:
        total_minutes = int(total_minutes)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours} hours {minutes} minutes"
    except (ValueError, TypeError):
        return "Invalid time"
