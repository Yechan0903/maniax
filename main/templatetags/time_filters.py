from django import template

register = template.Library()

@register.filter
def display_time(total_minutes):
    try:
        total_minutes = int(total_minutes)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        #if 0 <= hours < 10:
        #    hours = f"0{hours}"
        #if 0 <= minutes < 10:
        #    minutes = f"0{minutes}"
        return f"{hours}시간 {minutes}분"
    except (ValueError, TypeError):
        return "Invalid time"

@register.simple_tag
def time_comparison(goals, total_minutes):
    if goals > total_minutes:
        return "성공"
    else:
        return "실패"