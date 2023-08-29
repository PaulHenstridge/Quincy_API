from datetime import datetime

def apply_filters(query_set, start_date_string, end_date_string, min_length, max_length):
    if start_date_string:
        try:
            start_date = datetime.strptime(start_date_string, '%m-%y')
            query_set = query_set.filter(date_time__gte=start_date)
        except ValueError:
            return None, "Invalid date format.  Please use MM-YY"
    
    if end_date_string:
        try:
            end_date = datetime.strptime(end_date_string, '%m-%y')
            query_set = query_set.filter(date_time__lte=end_date)
        except ValueError:
            return None, "Invalid date format.  Please use MM-YY"
    
    if min_length:
        try:
            min_length = float(min_length)
            query_set = query_set.filter(length_mins__gte=min_length)
        except ValueError:
            return None, "Invalid minimum length.  Must be a number"
    
    if max_length:
        try:
            max_length = float(max_length)
            query_set = query_set.filter(length_mins__lte=max_length)
        except ValueError:
            return None, "Invalid maximum length.  Must be a number"
    
    return query_set, None