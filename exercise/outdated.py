months = [
    "January",
    "February", 
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Date: ").strip()
    
    try:
        # Try MM/DD/YYYY format first
        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) == 3:
                month, day, year = parts
                month = int(month)
                day = int(day)
                year = int(year)
        
        # Try "Month DD, YYYY" format
        elif "," in date_input:
            parts = date_input.split()
            if len(parts) == 3:
                month_name = parts[0]
                day = int(parts[1].rstrip(","))
                year = int(parts[2])
                
                if month_name in months:
                    month = months.index(month_name) + 1
                else:
                    raise ValueError("Invalid month name")
        else:
            raise ValueError("Invalid format")
        
        # Validate date ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        else:
            raise ValueError("Date out of range")
            
    except (ValueError, IndexError):
        continue
