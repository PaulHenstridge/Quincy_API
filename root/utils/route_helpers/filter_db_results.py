from datetime import datetime

def apply_filters(data, start_date_string, end_date_string, min_length, max_length):
    error = None

    if isinstance(data, list):
        if start_date_string:
            try:
                start_date = datetime.strptime(start_date_string, '%m-%y')
                data = [d for d in data if d.date_time >= start_date]
            except ValueError:
                return None, "Invalid date format. Please use MM-YY"
        
        if end_date_string:
            try:
                end_date = datetime.strptime(end_date_string, '%m-%y')
                data = [d for d in data if d.date_time <= end_date]
            except ValueError:
                return None, "Invalid date format. Please use MM-YY"
        
        if min_length:
            try:
                min_length = float(min_length)
                data = [d for d in data if d.length_mins >= min_length]
            except ValueError:
                return None, "Invalid minimum length. Must be a number"
        
        if max_length:
            try:
                max_length = float(max_length)
                data = [d for d in data if d.length_mins <= max_length]
            except ValueError:
                return None, "Invalid maximum length. Must be a number"
    else:

        if start_date_string:
            try:
                start_date = datetime.strptime(start_date_string, '%m-%y')
                data = data.filter(date_time__gte=start_date)
            except ValueError:
                return None, "Invalid date format.  Please use MM-YY"
        
        if end_date_string:
            try:
                end_date = datetime.strptime(end_date_string, '%m-%y')
                data = data.filter(date_time__lte=end_date)
            except ValueError:
                return None, "Invalid date format.  Please use MM-YY"
        
        if min_length:
            try:
                min_length = float(min_length)
                data = data.filter(length_mins__gte=min_length)
            except ValueError:
                return None, "Invalid minimum length.  Must be a number"
        
        if max_length:
            try:
                max_length = float(max_length)
                data = data.filter(length_mins__lte=max_length)
            except ValueError:
                return None, "Invalid maximum length.  Must be a number"
        
    return data, error